import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Regexp

from aiogram.utils.exceptions import InvalidHTTPUrlContent


from finder import find_books
from grabber import grab_book

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher(bot)

#Response to user

START_MESSAGE = "Hello! This bot will help to find any book that you need. Of course if it exist in our DataBase. Wish you good luck in using our bot ;) Made by: @lisatrot"

# Хэндлер на команду /start

links = []

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Поиск")
    keyboard.add(button)
    await message.answer(START_MESSAGE, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Поиск")
async def cmd_search(message):
    await message.reply("Enter name of your book")

    @dp.message_handler()
    async def show_books(message: types.Message):
        sender = str(message.text)
        data = find_books(sender)
        global links
        links = data[1]
        user_view = str()
        for i in data[0]:
            for j in i:
                user_view += j
                user_view += " "
            user_view += "\n"



        inline_keyboard = types.InlineKeyboardMarkup(row_width=5)
        buttons = [
            types.InlineKeyboardButton(str(x), callback_data=f'search-{x}') for x in range(1,11)
            ]
        
        inline_keyboard.add(*buttons)
        await message.reply(text=str(user_view), reply_markup=inline_keyboard)

@dp.callback_query_handler(Regexp(r"search-[1-9]|search-10"))
async def give_book(call: types.CallbackQuery): 
    query = call.data.split("-")
    await call.message.answer(f"Book #{str(query[1])}")
    global links
    number = int(query[1])
    calldata = number - 1
    link = grab_book(links[calldata])
    try:
        await call.message.reply_document(document=link)
    except InvalidHTTPUrlContent:
        await call.message.answer(text="Book is too big for tg, soon we'll bypass that ")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
