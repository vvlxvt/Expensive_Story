from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from services.notes_handling import get_categories, add_new_data
from keyboards.subname_kb import add_subname_kb
from lexicon.lexicon import LEXICON_FOOD, LEXICON_NONFOOD, LEXICON_SUBNAMES, LEXICON_CHOICE, LEXICON_KEYS, find_value
from database.queue import no_subs
from database.expense import Expense
from datetime import datetime

router: Router = Router()

@router.message()
async def add_note(message: Message):
    # обрабатывает любое сообщение пользователя с трат-ой/-ами
    # добавляет трату в БД
    row_message = message.text
    user_id = message.from_user.id
    all_subnames = get_categories(row_message, user_id)
    if all_subnames:
        await message.answer(f' добавлено в категории: <b>{all_subnames}</b>')
    if not no_subs.is_empty():
        await message.answer(text=f'добавить категорию товару <b>{no_subs.peek()[2]}</b>?',
                             reply_markup=add_subname_kb(**LEXICON_SUBNAMES))


@router.callback_query(F.data=='cancel')
async def cancel_add_expense(callback: CallbackQuery):
    top = no_subs.dequeue()[2]
    # реагирует на нажатие кнопки ДА для выбора категории товару
    if not no_subs.is_empty():
        await callback.message.edit_text(f'отменено действие для: <b>{top}</b>\nДобавить категорию товару: <b>'
                                         f'{no_subs.peek()[2]}</b>',
                                         reply_markup=add_subname_kb(**LEXICON_SUBNAMES))
    else:
        await callback.message.edit_text(f'отменено действие для: <b>{top}</b>')
        await callback.message.delete_reply_markup()


@router.callback_query(F.data=='food')
async def process_basic_food_press(callback: CallbackQuery):
    # реагирует на ключ "food"
    await callback.message.edit_text(text=f'выберите подкатегорию для <b>{no_subs.peek()[2]}</b>',
                                     reply_markup=add_subname_kb(**LEXICON_FOOD))
    await callback.answer()

@router.callback_query(F.data=='non_food')
async def process_basic_nonfood_press(callback: CallbackQuery):
    # реагирует на ключ "non_food"
    await callback.message.edit_text(text=f'выберите подкатегорию для <b>{no_subs.peek()[2]}</b>',
                                     reply_markup=add_subname_kb(**LEXICON_NONFOOD))
    await callback.answer()


@router.callback_query(F.data.in_(LEXICON_KEYS))
async def process_nonfood_press(callback: CallbackQuery):
    name = no_subs.peek()[0]
    sub_name = callback.data
    price = no_subs.peek()[1]
    today = datetime.now().replace(second=0, microsecond=0)
    raw_message = no_subs.peek()[2]
    user_id = callback.from_user.id
    flag = True
    expense = Expense(name, sub_name, price, today, raw_message, user_id, flag)
    add_new_data(expense)
    await callback.message.answer(text=f'{expense.name} добавлено в категорию <b>{expense.subname}</b>')
    no_subs.dequeue()
    if no_subs.is_empty():
        await callback.message.answer(text='✅ Все траты добавлены')
        await callback.answer()
    else:
        await callback.message.answer(f' выберите категорию для: <b>{no_subs.peek()[2]}</b>',
                                      reply_markup=add_subname_kb(**LEXICON_SUBNAMES))
        await callback.message.delete_reply_markup()

