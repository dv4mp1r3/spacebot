import asyncio
import logging
import os
import sys
import json

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from logic.data_providers import TransactionDataSource, ResidentDataSource, CsvDataSource
from logic.access_control import TelegramCsvBasedAccessControl
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import paho.mqtt.client as mqtt
from dotenv.main import load_dotenv

load_dotenv()

TOKEN = os.getenv('SWYNCA_API_TOKEN')
HOST = os.getenv('SWYNCA_API_HOST')
MQTT_URL = os.getenv('MQTT_URL')

scheduler = AsyncIOScheduler()
router = Router()
tg_access_control = TelegramCsvBasedAccessControl(CsvDataSource('residents.csv', ','))

class Form(StatesGroup):
    start = State()
    tranlog = State()
    open = State()


def on_connect(client, userdata, flags, rc):
    logging.info(f"mqtt connected with result code {str(rc)}")


if MQTT_URL != '':
    client = mqtt.Client()
    client.connect(MQTT_URL, 1883, 60)
    client.on_connect = on_connect


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Вы сбросили сохраненное состояние.",
        reply_markup=ReplyKeyboardRemove(),
    )

@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(f"Привет, <b>{message.from_user.full_name}!</b>"
                         " У меня ты можешь посмотреть лог транзакций, а оповещение об оплате я сделаю самостоятельно.")


@router.message(Command(commands=["tranlog"]))
async def command_transaction_log(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.tranlog)
    data_source = TransactionDataSource(HOST, TOKEN, message.from_user.id)
    if data_source.get_records_count() <= 0:
        await message.answer('На текущий момент нет записей в логе транзакций.')
        return
    answer = 'Список транзакций:\n'
    for record in data_source.get_records():
        summ = record.value / 100
        answer += f"{record.datetime} на сумму {summ}"
        if record.comment is not None and len(record.comment) > 0:
            answer += f"({record.comment})"
        answer += '\n'
    await message.answer(answer)


@router.message(Command(commands=["open"]))
async def commend_open_handler(message: Message, state: FSMContext) -> None:
    global tg_access_control
    if tg_access_control.allow_access(message.from_user.id) is False:
        await message.answer('Похоже, что у Вас нет прав на использование команды.')
    await state.update_data(name=message.text)
    await state.set_state(Form.open)
    await message.answer(
        'Точно нужно открыть дверь?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Да'),
                    KeyboardButton(text='Нет'),
                ]
            ],
            resize_keyboard=True
        ),
    )


@router.message(Form.open, F.text.casefold() == 'да')
async def open_the_door(message: Message, state: FSMContext) -> None:
    if ('client' in globals()) is False:
        await message.reply('Бот запущен без возможности открывать двери :(')
        return
    global client
    await state.set_state(Form.start)
    if client.is_connected() is False:
        client.reconnect()
    try:
        publish_result = client.publish('bus/telegram/message', json.dumps({'userid': message.from_user.id}))
        if publish_result.is_published() is False:
            raise IOError('mqtt publish_result._published is False')
    except (ValueError, TypeError, IOError) as err:
        await message.reply('Что-то пошло не так при отправке mqtt-сообщения :( Дверь не откроется. ')
        logging.error('mqtt publish error')
        logging.error(err)
        return
    await message.reply(
        f"*вы слышите шорох механизма в соседней комнате*"
        f"\n\n"
        f"{message.from_user.username} открыл оранжевую дверь.",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Form.open, F.text.casefold() == "нет")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Хорошо, открою как-нибудь потом.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.open)
async def process_unknown_write_bots(message: Message, state: FSMContext) -> None:
    await message.reply('Принимаются только ответы "Да" или "Нет"')


@router.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer("/start - сброс состояния (начало работы бота)\n"
                         "/tranlog - показ лога транзакций\n"
                         "/open - открытие двери (потребуется дополнительное подтверждение)")


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(os.getenv('TG_BOT_TOKEN'), parse_mode="HTML")
    scheduler.add_job(send_deposit_notifications, "cron", day=1, minute=0, args=(dp, bot))
    scheduler.start()
    await dp.start_polling(bot)


async def send_deposit_notifications(dp: Dispatcher, bot):
    data_source = ResidentDataSource(HOST, TOKEN)
    if data_source.get_records_count() <= 0:
        return
    for record in data_source.get_records():
        if record.debt <= 0:
            continue
        summ = record.debt / 100
        await bot.send_message(chat_id=record.id, text=f"Необходимо пополнить баланс на {summ} рублей")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
