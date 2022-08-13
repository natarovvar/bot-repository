
from keyboards import kb_client
from aiogram import types, md
from aiogram import Dispatcher
from create import dp, bot
from database import sqlite_database
from database.sqlite_database import sql_add_geopostition

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils.executor import start_polling
from aiogram.utils.markdown import bold, code, italic, text

import aiohttp


""" @dp.message_handler(commands=['g']) #дикоратор
async def g_func(message: types.Message):
    place = "Красная площадь, Москва"
    location = GoogleV3(api_key="AIzaSyBAYdzyr-4Bwr9nwThuvhaPv9RGfmKlK58", domain="maps.google.ru").geocode(place)
    await message.answer(location.address)
    message.answer(location.latitude, location.longitude)
"""

#@dp.message_handler(commands=['start','help']) #дикоратор
async def send_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\n")
    await message.answer("Работаю над ботом, добавляю обработчики команд и разбираюсь в БД\n\n🔸Мне доступны команды:\n - /dice\n- /load (Загрузка объекта - фотографий и их описаний)\n- /getlocation \n\n 🔸Update v.0.0.1 \n- добавил выход из состояния /load с помощью команды /выход (в случае ошибки или если пользователь не захочет дальше что либо вводить)\n - немного расширил фильтр нецензурных слов\n - бот может ответить на любое сообщение в контексте которого присутствует слово 'бот'/'тупой'\n\n 🔸Update v.0.0.2\n- добавлена команда /getlocation (геопозицию можно передать через мобильное приложение telegram, ПК геопозицию не поддерживают)")

@dp.message_handler(commands=['testp'])
async def cmd_test(message: types.Message):
    await message.answer(message.message_id)
    await message.answer(message.date)
    await message.answer(message.chat)
    await message.answer(message.from_user.full_name)
    async with aiohttp.ClientSession() as session:
        ip = await fetch(GET_IP_URL, session)
        content.append(text(':globe_showing_Americas:', bold('IP:'), code(ip)))
    
    
    
    
#@dp.message_handler(commands='dice')
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲",reply_markup=kb_client)

async def cmd_location_text(message: types.Message):
    global uname 
    await message.answer('Отправьте свою геопозицию')
    uname = message.from_user.full_name

async def cmd_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await sqlite_database.sql_add_geopostition(uname,lat, lon)
    await message.answer(reply)

    


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_start,commands=['start','help'])
    dp.register_message_handler(cmd_dice,commands=['dice'])
    dp.register_message_handler(cmd_location,content_types=['location'])
    dp.register_message_handler(cmd_location_text,commands = ['getlocation'])
    