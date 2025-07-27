from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from bot.keyboards.language import get_language_keyboard
from services.language import get_message
from data.database import Session, init_db
from data.models.user import User

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    init_db()
    with Session() as session:
        user = session.get(User, message.from_user.id)
        if not user:
            user = User(
                user_id=message.from_user.id,
                name=message.from_user.full_name,
                language="en"
            )
            session.add(user)
            session.commit()


    await message.answer(
        get_message("fa", "welcome"),
        reply_markup=get_language_keyboard()
    )


@router.callback_query(lambda c: c.data in ["lang_fa", "lang_en"])
async def handle_message_selection(callback: CallbackQuery):
    lang_code = "fa" if callback.data == "lang_fa" else "en"
    lang_name = "فارسی" if lang_code == "fa" else "English"
    with Session() as session:
        user = session.get(User, callback.from_user.id)
        if user:
            user.language = lang_code
            session.commit()
    await callback.message.answer(get_message(lang_code, "language_selected"))
    await callback.message.delete()
    await callback.answer()