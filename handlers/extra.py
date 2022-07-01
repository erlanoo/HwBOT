from aiogram import types, Dispatcher

from config import bot


# async def echo_message(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)
    x = message.text
    try:
        x = int(x)
        c = 1
    except ValueError:
        await bot.send_message(message.chat.id, 'Value error, try again!')
        c = 0
    if c == 1:
        await bot.send_message(message.chat.id, f"{x * x}")
    elif c == 0:
        await bot.send_message(message.chat.id, x)
    else:
        pass


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
    # dp.register_message_handler(echo_message)
