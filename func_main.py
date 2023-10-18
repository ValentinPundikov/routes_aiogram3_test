from aiogram import Bot, Dispatcher
from config.config import TOKEN_TELEGRAM
import functions.functions
import functions.admin_functions
import functions.users_functions


async def main():
    bot = Bot(token=TOKEN_TELEGRAM)
    dp = Dispatcher()
    dp.include_routers(functions.functions.router)
    dp.include_routers(functions.users_functions.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

