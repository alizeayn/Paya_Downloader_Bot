from aiogram import Router, F
from aiogram.types import Message
from services.language import get_message
from data.database import Session
from data.models.user import User
import re

router = Router()
youtube_regex = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")

@router.message(F.text.regexp(youtube_regex).as_("match"))
async def handle_youtube_link(message: Message, match: re.Match):
    with Session() as session:
        user = session.get(User, message.from_user.id)
        language = user.language if user else "en"
    if match:
        await message.answer(get_message(language, "valid_link"))
    else:
        await message.answer(get_message(language, "invalid_link"))
