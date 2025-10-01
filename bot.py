import asyncio
import datetime
import logging
import os
import sys
import json
import uuid

from aiogram.methods import AnswerCallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, FSInputFile, CallbackQuery

import openapi_client
from logic.data_providers import BalanceFromReSwynca, TransactionsFromReSwynca, BaseDataSource, \
    ActiveMembersFromReSwyncaDataSource
from logic.access_control import DebugAlwaysAllowAccessControl
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import paho.mqtt.client as mqtt
from dotenv.main import load_dotenv
from aiogram.utils.keyboard import InlineKeyboardBuilder

from openapi_client import MemberDTO, CreateMemberTransactionDTO

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


def is_valid_guid(guid_str: str) -> bool:
    try:
        uuid.UUID(guid_str)
        return True
    except ValueError:
        return False


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
    file = await message.document.bot.get_file(message.document.file_id)
    dest = f"/tmp/{message.document.file_name}"
    await message.document.bot.download_file(file.file_path, destination=dest)
    with open(dest, mode="r", encoding="utf-8") as f:
        content = f.read()
        cached_tran_log[str(message.from_user.id)] = content.splitlines()
    await member_tran_with_inline_keyboard_answer(message=message, state=state)


def get_answer_object(query: CallbackQuery = None, message: Message = None) -> Message:
    if query is not None:
        return query.message
    else:
        return message


def get_user_id(query: CallbackQuery = None, message: Message = None) -> int:
    if query is not None:
        return query.from_user.id
    return message.from_user.id


async def query_answer(query: CallbackQuery = None) -> AnswerCallbackQuery:
    if query is not None:
        return await query.answer()
    return None


async def member_tran_with_inline_keyboard_answer(
        state: FSMContext,
        query: CallbackQuery = None,
        message: Message = None,
        create_tran_result: str = ''
) -> None:
    tran_data_str = ''
    answer_object = get_answer_object(query, message)
    user_id = str(get_user_id(query, message))

    while len(cached_tran_log[user_id]) > 1:
        line = cached_tran_log[user_id].pop()
        elements = line.split('";"')
        if elements[6] == '':
            continue
        elements[6] = elements[6].replace(',', '.').replace(' ', '')
        elements[0] = elements[0].replace('"', '')
        tran_data_str = f'{create_tran_result}Новая транзакция. Дата транзакции: {elements[0]}, сумма {elements[6]}, примечание ({elements[9]}).' \
                        f' Выбери резидента:'
        tran = {
            'type': 'deposit',
            'source': 'topup',
            'target': None,
            'comment': 'debug topup from spacebot',
            'amount': str(elements[6]),
            'date': '2025-10-01T10:11:00.000Z',
        }
        break
    if len(tran_data_str) == 0:
        del_cached_tran_log_by_user_id(str(get_user_id(query, message)))
        await state.clear()
        await answer_object.answer('Закончили обрабатывать файл')
        await query_answer(query)
        return
    data_source = ActiveMembersFromReSwyncaDataSource(host=HOST, access_token=TOKEN, user_id=user_id)
    records = data_source.get_records()
    if len(records) > 0:
        builder = fill_inline_keyboard_by_active_members(records, tran, user_id)
        await state.set_state(Form.csv_parse_line)
        await answer_object.answer(
            text=tran_data_str,
            reply_markup=builder.as_markup()
        )
    else:
        await state.clear()
        await answer_object.answer('В свинке нет записей о резидентах')
    await query_answer(query)


def del_cached_tran_log_by_user_id(user_id: int) -> None:
    uid = str(user_id)
    to_remove = []

    for key in cached_tran_log.keys():
        if isinstance(key, str) and key.startswith(uid):
            to_remove.append(key)
    for key in to_remove:
        del cached_tran_log[key]
    if uid in cached_tran_log:
        del cached_tran_log[uid]


@router.callback_query(StateFilter(Form.csv_parse_line))
async def parse_csv_line(query: CallbackQuery, state: FSMContext) -> None:
    create_tran_result = ''
    data = query.data.lstrip('tran:')
    if data == 'break':
        del_cached_tran_log_by_user_id(str(get_user_id(query, None)))
        await state.clear()
        await query.message.answer('Обработка файла остановлена')
        await query.answer()
        return
    if is_valid_guid(data):
        re_swynca_config = openapi_client.Configuration(host=HOST)
        api_client = openapi_client.ApiClient(configuration=re_swynca_config)
        api_client.set_default_header("Authorization", "Bearer " + TOKEN)
        tran_api = openapi_client.MemberTransactionsApi(api_client)
        tran = cached_tran_log[data]
        del cached_tran_log[data]
        tran_object = CreateMemberTransactionDTO.from_dict(tran)
        create_result = tran_api.member_transactions_controller_create(tran_object)
        if create_result is None or create_result.actor is None:
            create_tran_result = 'something wrong'
        else:
            create_tran_result = f'Баланс резидента пополнен на {tran_object.amount}р.'
    await member_tran_with_inline_keyboard_answer(query=query, state=state, create_tran_result=create_tran_result)


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


def fill_inline_keyboard_by_active_members(records: list[MemberDTO], tran: dict, user_id: str) \
        -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for r in records:
        guid = str(uuid.uuid4())
        key = f'{user_id}-{guid}'
        cached_tran_log[key] = tran.copy()
        cached_tran_log[key]['subjectId'] = r.id
        builder.button(
            text=f'{r.telegram_metadata.telegram_name} ({r.name})',
            callback_data=f"tran:{key}"
        )
    builder.button(text=f'Пропустить запись', callback_data=f"tran:skip")
    builder.button(text=f'Прекратить обработку', callback_data=f"tran:break")
    builder.adjust(1)
    return builder


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
