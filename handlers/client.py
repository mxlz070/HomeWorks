from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keybort.client_kb import start_markup
from database.bot_db import sql_command_random, sql_command_all
from keybort.client_kb import direction_markup


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!", reply_markup=start_markup)


async def pin_chat_command(message: types.Message):
    if message.chat.type != 'private':
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message_id=message.reply_to_message.message_id)
        else:
            await message.answer('Сообщение должно быть ответом умник!')
    else:
        await message.answer('Пиши в группе чел!')


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Сам разбирайся баурым!')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать брат!",
        open_period=5,
        reply_markup=markup
    )

async def get_random_user(message: types.Message):
    # await message.answer("Какое направление?", reply_markup=direction_markup)
    await sql_command_random(message)


async def get_all_mentor(message: types.Message):
    await sql_command_all()
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_chat_command, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=["getmentor"])
    dp.register_message_handler(get_all_mentor, commands=["allmentor"])