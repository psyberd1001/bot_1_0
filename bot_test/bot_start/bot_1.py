from aiogram import Dispatcher, Bot
import asyncio
from bot_test.handlers1 import start
import logging
from bot_test.config.config import bot_token



async def main():
    bot = Bot(bot_token)
    dp = Dispatcher()
    dp.include_routers(start.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

