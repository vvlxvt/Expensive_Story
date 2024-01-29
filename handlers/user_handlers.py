from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON, LEXICON_MONTH, LEXICON_ANOTHER
from keyboards import add_subname_kb, another_kb
from database import *
from filters import IsAdmin
from bot import ADMIN_IDS

router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='del_last_note'),(IsAdmin(ADMIN_IDS)))
async def del_note(message: Message):
    last = del_last_note()
    text = 'удалена запись: '
    await message.answer( text=text+last)


@router.message(Command(commands='today'),(IsAdmin(ADMIN_IDS)))
async def get_today(message: Message):
    message_date = message.date
    total_spending = spend_today()
    date_format = '%d-%m-%Y'  # Формат часов:минут:секунд
    formatted_time = message_date.strftime(date_format)
    await message.answer(text=f'сегодня <i>{formatted_time}</i> потрачено <b>{total_spending}</b> GEL ')

@router.message(Command(commands='week'),(IsAdmin(ADMIN_IDS)))
async def get_week(message: Message):
    res = get_stat_week()
    total = round(spend_week(),2)
    await message.answer(text=f'  <b>{res}</b>\n С начала недели потрачено: {total} GEL ')

@router.message(Command(commands='month'),(IsAdmin(ADMIN_IDS)))
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
    month = callback.data
    res = get_stat_month(month)
    total = spend_month(month)
    name_month = LEXICON_MONTH[callback.data]
    await callback.message.edit_text(
        text=f'<u>Траты за <b>{name_month}</b>:</u> \n{res}\n<b> ИТОГО: {total}</b> gel')
    await callback.message.answer(text=f'Показать подробно категорию ДРУГОЕ?')
    await callback.message.answer(text=month, reply_markup=another_kb(**LEXICON_ANOTHER))

@router.callback_query(F.data=='_another')
async def show_another(callback: CallbackQuery):
    month = callback.message.text
    start_date, end_date = get_month_range(month)
    result = get_another(start_date, end_date)
    await callback.message.answer(
        text=f'<u>Другое за <b>{LEXICON_MONTH[month]}</b>:</u> \n{result}\n')
    await callback.message.delete_reply_markup()

@router.callback_query(F.data=='_cancel')
async def cancel_add_expense(callback: CallbackQuery):
        await callback.message.edit_text(text = 'отмена')
        await callback.message.delete_reply_markup()

