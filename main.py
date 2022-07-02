import asyncio
from database import bot_db
from aiogram.utils import executor
from config import dp, bot, URL
from handlers import admin, notifiation, client, extra, callback, FSMAdmin
import logging
from decouple import config
async def on_startup(_):
    await bot.set_webhook(URL)
    bot_db.sql_create()
    asyncio.create_task(notifiation.scheduler())


async def on_shutdown(dp):
    await bot.delete_webhook()

notifiation.register_handler_notifiation(dp)
FSMAdmin.register_handler_fsm_dish(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_hundler_admin(dp)
extra.register_handlers_extra(dp)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int))

    #executor.start_polling(dp, skip_updates=True,on_startup=on_startup)