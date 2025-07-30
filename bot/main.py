from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers.start import router as start_router
from dotenv import load_dotenv
from data.database import init_db
from bot.handlers.link import router as link_router
import os
import asyncio

load_dotenv()

async def main():
    init_db()
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start_router)
    dp.include_router(link_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())