from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


button1 = KeyboardButton('/dice')
button2 = KeyboardButton('Отправить своё положение 🗺️', request_location=True)
ibutton1 = InlineKeyboardButton(text='delete',url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
ibutton1 = InlineKeyboardButton(text='unload',url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
x = [InlineKeyboardButton(text='xabr',url='https://habr.com/ru/all/?ysclid=l6v8716gpv651661317'),\
    InlineKeyboardButton(text='wiki',url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')]

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)
ikb_client = InlineKeyboardMarkup(row_width=2)
idb_client = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='delete',callback_data='del'),\
                                               InlineKeyboardButton(text='unload',callback_data='uload'     ))



kb_client.add(button1).add(button2)
ikb_client.row(*x)


