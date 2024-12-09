import logging

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from app.bot.lexicons.lexicon import BUTTONS

logger = logging.getLogger(__name__)

buttons = {
    '<<': '-1',
    f'1/{len(BUTTONS)+1}': '/bookmarks',
    '>>': '1'
}

def load_inline_keyboard(size: tuple[int, ...] = (3,), **kwargs: str) -> InlineKeyboardMarkup:

    keyboard = InlineKeyboardBuilder()
    for button, call in kwargs.items():
        keyboard.button(text=button, callback_data=call)

    keyboard.adjust(*size)
    return keyboard.as_markup()