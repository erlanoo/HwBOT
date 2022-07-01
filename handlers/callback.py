from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


# @dp.callback_query_handler(lambda coll: coll.data == "button_call_1")
async def quez_2(coll: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Когда Адольф Гитлер совершил самоубийтво?"
    answers = [
        "30-апреля,1945-году",
        "29-апреля,1945году",
        "28-апрель,1945-году",
        "1945-году",
    ]
    await bot.send_poll(
        chat_id=coll.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call4 = InlineKeyboardButton("next", callback_data="button_call4")
    markup.add(button_call4)
    question1 = "Кто создал ноутбук?"
    answers1 = [
        "Уильям Моггридж",
        "Чарлз Бэббидж",
        "Карл Фердинанд Браун",
        "Крисофер Латэм Шоулз",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question1,
        options=answers1,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


async def q_1(call: types.CallbackQuery):
    await bot.send_message(
        call.message.chat.id,
        "Бишоп-Рок, Добро пожаловать",
    )


async def q_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton("Токио 🇯🇵", callback_data="button_call_7")
    button_call_8 = InlineKeyboardButton("Манила 🇵🇭", callback_data="button_call_8")
    markup.add(button_call_7, button_call_8)

    await bot.send_message(
        call.message.chat.id, "в какой город хочешь полететь?", reply_markup=markup
    )


async def q_3(call: types.CallbackQuery):
    await bot.send_message(
        call.message.chat.id,
        "Добро пожаловать в Страну Восходящего Солнце",
    )


async def q_4(call: types.CallbackQuery):
    await bot.send_message(
        call.message.chat.id,
        "добро Пожаловать В город Манила",
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
        quez_2, lambda coll: coll.data == "button_call_1"
    )
    dp.register_callback_query_handler(quiz3, lambda coll: coll.data == "button_call_2")
    dp.register_callback_query_handler(q_1, lambda coll: coll.data == "button_call_5")
    dp.register_callback_query_handler(q_2, lambda coll: coll.data == "button_call_6")
    dp.register_callback_query_handler(q_3, lambda coll: coll.data == "button_call_7")
    dp.register_callback_query_handler(q_4, lambda coll: coll.data == "button_call_8")
