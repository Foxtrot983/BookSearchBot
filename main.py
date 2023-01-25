#5914047175:AAFA-S9m_UJsseXP20UYgkut9dG7eeRQkj4
#from background import keep_alive
#import pip
#pip.main(["install", "aiogram"])

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
bot = Bot(token="5823422980:AAGUBH4ZQCOyWvAbha5wLaj5Htq0SGIWM1w")
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
        #def books_output(result):
#Test#
        #    message.reply(result)
        #    pass
        global links
        links = data[1]
        user_view = str()
        for i in data[0]:
            for j in i:
                user_view += j
                user_view += " "
            user_view += "\n"



        #await message.reply(find_books(sender))
        inline_keyboard = types.InlineKeyboardMarkup(row_width=5)
        #button1 = types.InlineKeyboardButton("1", callback_data='btn1')
        #button2 = types.InlineKeyboardButton("2", callback_data='btn2')
        #button3 = types.InlineKeyboardButton("3", callback_data='btn3')
        #button4 = types.InlineKeyboardButton("4", callback_data='btn4')
        #button5 = types.InlineKeyboardButton("5", callback_data='btn5')
        #button6 = types.InlineKeyboardButton("6", callback_data='btn6')
        #button7 = types.InlineKeyboardButton("7", callback_data='btn7')
        #button8 = types.InlineKeyboardButton("8", callback_data='btn8')
        #button9 = types.InlineKeyboardButton("9", callback_data='btn9')
        #button10 = types.InlineKeyboardButton("10", callback_data='btn10')
        #inline_buttons = [button1, button2, button3, button4, button5, 
        #button6, button7, button8, button9, button10]
        buttons = [
            types.InlineKeyboardButton(str(x), callback_data=f'search-{x}') for x in range(1,11)
            ]
        
        inline_keyboard.add(*buttons)
        #b1 = types.InlineKeyboardButton("first button", callback_data="btn1")
        #buttons = (b1,)
        #inline_keyboard = types.InlineKeyboardMarkup().add(*buttons)
        #b2 = types.InlineKeyboardButton('2')
        #inline_keyboard.add(b1)
        #Добавить кнопки с выбором номера результата и привязать к выводу
        #result переделать в стринг
        await message.reply(text=str(user_view), reply_markup=inline_keyboard)

#сделать что-то вроде [r"search-[1-9]|search-10"] и
@dp.callback_query_handler(Regexp(r"search-[1-9]|search-10")) #переделать коллбэк_дата кнопок
async def give_book(call: types.CallbackQuery): #Искомое - это call.data
    #await call.message.answer(str(call.message))
    query = call.data.split("-")
    await call.message.answer(f"Book #{str(query[1])}")
    global links
    number = int(query[1])
    #await call.message.answer(str(links))
    calldata = number - 1
    link = grab_book(links[calldata])
    #book = types.MediaGroup()
    #book.attach_document(open(link, 'rb'))
    #await message.reply_media_group(book)
    #file = types.input_file.InputFile()
    try:
        await call.message.reply_document(document=link)
    except InvalidHTTPUrlContent:
        await call.message.answer(text="Book is too big for tg, soon we'll bypass that ")


        #@dp.message_handler()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
