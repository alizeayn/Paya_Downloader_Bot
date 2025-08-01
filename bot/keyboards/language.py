from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_language_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="فارسی", callback_data="lang_fa"),
            InlineKeyboardButton(text="English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)