import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from config import TOKEN
from routes import router

bot = Bot(token=os.environ.get(TOKEN))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
