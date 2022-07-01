import random

from aiogram import types, Dispatcher
from config import bot, ADMIN


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMIN:
            await message.answer("Ты не Админ!")
        elif not message.reply_to_message:
            await message.answer("команда должно быть ответом на сообщение!")
        else:
            await message.bot.kick_chat_member(
                message.chat.id, user_id=message.reply_to_message.from_user.id
            )
            await message.answer(
                f"пользователь {message.reply_to_message.from_user.full_name}"
                f" был забанен по воле {message.from_user.full_name}"
            )


async def game(message: types.Message):
    games = ["⚽", "⚾", "🏓", "🎯", "🎲", "🎰"]
    value = random.choice(games)
    if message.text.startswith("game"):
        await bot.send_message(message.chat.id, value)


def register_hundler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")
    dp.register_message_handler(game,commands=['game'])
