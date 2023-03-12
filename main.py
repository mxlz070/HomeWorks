from decouple import config
from aiogram import Bot,Dispatcher,types
from aiogram.utils import  executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Кто лучший препод?"
    answer = [
        "Airas",
        "Bekbolot",
        "Esen",
        "igor",
        "Nurlan",
        "Aleksey",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Сколько областей в Кыргызстане?"
    answer = [
        "12",
        "3",
        "7",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
    )

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello bro!')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Сам разбирайся брат!')

@dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    photos = (
        'media/mem1.jpg',
        'media/mem2.jpg',
        'media/mem3.jpg',
        'media/mem4.jpg',
        'media/mem5.jpg',
        'media/mem6.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id,photo)
@dp.message_handler()
async def echo_command(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

