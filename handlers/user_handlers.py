from database.conn_db import del_last_note, get_stat_month, get_stat_week
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON, LEXICON_MONTH
from keyboards.subname_kb import add_subname_kb
from database.conn_db import spend_today, spend_week, get_my_expenses

router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='del_last_note'))
async def del_note(message: Message):
    last = del_last_note()
    text = 'удалена запись: '
    await message.answer( text=text+last)


@router.message(Command(commands='today'))
async def get_today(message: Message):
    message_date = message.date
    total_spending = spend_today()
    date_format = '%d-%m-%Y'  # Формат часов:минут:секунд
    formatted_time = message_date.strftime(date_format)
    await message.answer(text=f'сегодня <i>{formatted_time}</i> потрачено <b>{total_spending}</b> GEL ')

@router.message(Command(commands='week'))
async def get_week(message: Message):
    res = get_stat_week()
    total = round(spend_week(),2)
    await message.answer(text=f'  <b>{res}</b>\n С начала недели потрачено: {total} GEL ')

@router.message(Command(commands='month'))
async def get_month(message: Message):
    text = 'За какой месяц показать статистику?'
    await message.answer( text=text, reply_markup=add_subname_kb(**LEXICON_MONTH))

@router.message(Command(commands='my_10'))
async def get_month(message: Message):
    user_id = message.from_user.id
    result = get_my_expenses(user_id)
    text = 'Мои последние 10 трат: '
    await message.answer( text = f' {text}\n {result} ')

@router.callback_query(F.data.in_(LEXICON_MONTH.keys()))
async def process_chose_month(callback: CallbackQuery):
    res = get_stat_month(callback.data)
    month = LEXICON_MONTH[callback.data]
    await callback.message.delete_reply_markup()
    await callback.message.answer(text=f'<u>Траты за <b>{month}</b>:</u> \n{res}')



