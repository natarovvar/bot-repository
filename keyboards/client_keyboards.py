from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardRemove

button1 = KeyboardButton('/dice')
button2 = KeyboardButton('Отправить своё положение 🗺️', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.add(button1).add(button2)
