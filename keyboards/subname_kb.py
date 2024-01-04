from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_CHOICE

def add_subname_kb(**kwargs: dict[str, str]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button, text in kwargs.items():
        buttons.append(InlineKeyboardButton(text=text, callback_data=button))

        # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=2)

    kb_builder.row(InlineKeyboardButton(text=LEXICON_CHOICE['cancel'], callback_data='cancel'),width=1)
    return kb_builder.as_markup()





