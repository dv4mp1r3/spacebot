import asyncio
import logging
import os
import sys
import json
import uuid

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, FSInputFile, CallbackQuery
from logic.data_providers import BalanceFromReSwynca, TransactionsFromReSwynca, BaseDataSource, \
    ActiveMembersFromReSwyncaDataSource
from logic.access_control import DebugAlwaysAllowAccessControl
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import paho.mqtt.client as mqtt
from dotenv.main import load_dotenv
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()

TOKEN = os.getenv('SWYNCA_API_TOKEN')
HOST = os.getenv('SWYNCA_API_HOST')
MQTT_URL = os.getenv('MQTT_URL')
GOOGLE_SHEET_URL = os.getenv('GOOGLE_SHEET_URL')

scheduler = AsyncIOScheduler()
router = Router()
tg_access_control = DebugAlwaysAllowAccessControl()
cached_answers = dict()
cached_tran_log = dict()


def get_cached_data(command: str, username: str) -> str:
    key = f'{command}-{username}'
    if key in cached_answers:
        return cached_answers[key]
    return ''


def set_cached_data(command: str, username: str, data: str):
    key = f'{command}-{username}'
    cached_answers.update({key: data})


class Form(StatesGroup):
    start = State()
    tranlog = State()
    balance = State()
    open = State()
    csv = State()
    csv_parse_line = State()


def on_connect(client, userdata, flags, rc):
    logging.info(f"mqtt connected with result code {str(rc)}")


def mock_username(real_username: str) -> str:
    from_env_username = os.getenv('DEBUG_TG_USERNAME')
    if len(from_env_username) > 0:
        return from_env_username
    return real_username


def gen_random_string(length: int = 10) -> str:
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:length]


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
    username = mock_username(message.from_user.username)
    answer = get_cached_data(command='tranlog', username=username)
    if len(answer) <= 0:
        data_source = TransactionsFromReSwynca(host=HOST, access_token=TOKEN, user_id=str(message.from_user.id))
        if data_source.get_records_count() <= 0:
            await message.answer('На текущий момент нет записей в логе транзакций.')
            return
        answer = 'Список транзакций:\n'
        for record in data_source.get_records():
            answer += f"{record.var_date} на сумму {record.amount}"
            if record.comment is not None and len(record.comment) > 0:
                answer += f"({record.comment})"
            answer += '\n'
        # set_cached_data(command='tranlog', username=username, data=answer)
    if len(answer) > 4096:
        filepath = f'/tmp/{username}-{gen_random_string()}.log'
        f = open(filepath, "a")
        f.write(answer)
        f.close()
        await message.answer_document(
            document=FSInputFile(path=filepath, filename=f'{username}.log'),
            caption='Транзакций слишком много, поэтому отправлены в файле'
        )
        os.remove(filepath)
        return
    await message.answer(answer)


@router.message(Command(commands=["balance"]))
async def command_balance(message: Message, state: FSMContext) -> None:
    empty_balance_answer = 'На текущий момент нет записей по балансу.'
    await state.set_state(Form.balance)
    user_id = f'@{mock_username(message.from_user.username)}'
    answer = get_cached_data('balance', user_id)
    if len(answer) <= 0:
        data_source = BalanceFromReSwynca(host=HOST, access_token=TOKEN, user_id=str(message.from_user.id))
        records = data_source.get_records()
        if len(records) < 1:
            # set_cached_data(command='balance', username=user_id, data='')
            await message.answer(empty_balance_answer)
            return
        answer = records[0][str(message.from_user.id)]
        if len(answer) < 1:
            set_cached_data(command='balance', username=user_id, data=answer)
            await message.answer(empty_balance_answer)
            return
        set_cached_data(command='balance', username=user_id, data=answer)
    await message.answer(f'Баланс {answer}')


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


@router.message(Command(commands=['csv']))
async def request_csv(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.csv)
    await message.answer('Отправь следующим сообщением файл с транзакциями или /cancel для отмены')


@router.message(StateFilter(Form.csv), F.document)
async def parse_csv(message: Message, state: FSMContext) -> None:
    doc = message.document
    file_id = doc.file_id
    file_name = doc.file_name
    file = await doc.bot.get_file(file_id)
    file_path = file.file_path
    dest = f"/tmp/{file_name}"
    await doc.bot.download_file(file_path, destination=dest)
    with open(dest, mode="r", encoding="utf-8") as f:
        content = f.read()
        cached_tran_log[message.from_user.id] = content.splitlines()
    while len(cached_tran_log[message.from_user.id]) > 1:
        line = cached_tran_log[message.from_user.id].pop()
        elements = line.split('";"')
        if elements[6] == '':
            continue
        elements[6] = elements[6].replace(',', '.').strip()
        tran_data_str = f'Дата транзакции: {elements[0]}, сумма {elements[6]}, примечание ({elements[9]}). Выбери резидента'
        break
    data_source = ActiveMembersFromReSwyncaDataSource(host=HOST, access_token=TOKEN, user_id=str(message.from_user.id))
    records = data_source.get_records()
    if len(records) > 0:
        builder = InlineKeyboardBuilder()
        await state.set_state(Form.tran_add_member)
        for r in records:
            builder.button(text=f'{r.telegram_metadata.telegram_name} ({r.name})', callback_data=f"tran:{r.id}")
        builder.adjust(1)
        await message.answer(
            text=tran_data_str,
            reply_markup=builder.as_markup()
        )
    else:
        await state.clear()
        await message.answer('В свинке нет записей о резидентах')
    await state.set_state(Form.csv_parse_line)


@router.callback_query(StateFilter(Form.csv_parse_line))
async def parse_csv_line(query: CallbackQuery, state: FSMContext) -> None:
    tran_data_str = ''
    while len(cached_tran_log[query.from_user.id]) > 1:
        line = cached_tran_log[query.from_user.id].pop()
        elements = line.split('";"')
        if elements[6] == '':
            continue
        elements[6] = elements[6].replace(',', '.').strip()
        tran_data_str = f'Дата транзакции: {elements[0]}, сумма {elements[6]}, примечание ({elements[9]}). Выбери резидента'
        break
    if len(tran_data_str) == 0:
        await state.clear()
        await query.message.answer('Закончили обрабатывать документ')
        await query.answer()
        return
    data_source = ActiveMembersFromReSwyncaDataSource(host=HOST, access_token=TOKEN, user_id=str(query.from_user.id))
    records = data_source.get_records()
    if len(records) > 0:
        builder = InlineKeyboardBuilder()
        await state.set_state(Form.tran_add_member)
        for r in records:
            builder.button(text=f'{r.telegram_metadata.telegram_name} ({r.name})', callback_data=f"tran:{r.id}")
        builder.adjust(1)
        await state.set_state(Form.csv_parse_line)
        await query.message.answer(
            text=tran_data_str,
            reply_markup=builder.as_markup()
        )
    else:
        await state.clear()
        await query.message.answer('В свинке нет записей о резидентах')
    await query.answer()


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
    if os.getenv('ENABLE_DEPOSIT_NOTIFICATIONS') == '1':
        scheduler.add_job(send_deposit_notifications, "cron", day=1, minute=0, args=(dp, bot))
        scheduler.start()
    await dp.start_polling(bot)


async def send_deposit_notifications(dp: Dispatcher, bot):
    data_source = BaseDataSource()

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
