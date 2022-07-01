import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="got your id")


async def go_study():
    await bot.send_message(chat_id=chat_id, text="Пора Учиться")

async def scheduler():
    aioschedule.every().week.do(go_study)


    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notifiation(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "скажи" in word.text)