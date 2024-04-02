from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_book
from services import book


def create_pagination_keyboard(page=1)->InlineKeyboardMarkup:
    middle_button = f'{page}/{len(book)}'
    buttons = ['backward', middle_button, 'forward']
    if page == 1:
        buttons = buttons[1:]
    elif page == len(book):
        buttons = buttons[:-1]
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_book.get(button, button),
        callback_data=button) for button in buttons])
    return kb_builder.as_markup()