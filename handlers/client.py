
from keyboards import kb_client,idb_client,ikb_client
from aiogram import types, md
from aiogram import Dispatcher
from create import dp, bot
from database import sqlite_database
from database.sqlite_database import sql_add_geopostition

""" @dp.message_handler(commands=['g']) #дикоратор
async def g_func(message: types.Message):
    place = "Красная площадь, Москва"
    location = GoogleV3(api_key="AIzaSyBAYdzyr-4Bwr9nwThuvhaPv9RGfmKlK58", domain="maps.google.ru").geocode(place)
    await message.answer(location.address)
    message.answer(location.latitude, location.longitude)
"""

#@dp.message_handler(commands=['start','help']) #дикоратор
async def send_start(message: types.Message):
    await message.answer(f"Привет, <b>{message.from_user.first_name}</b>!\n",parse_mode=types.ParseMode.HTML)
    await message.answer("Бот находится в разработке\n\n🔸Мне доступны команды:\n - /dice\n- /load (Загрузка объекта - фотографий и их описаний)\n- /getlocation \n\n 🔸<code>Update v.0.0.1</code> \n- добавил выход из состояния /load с помощью команды /выход (в случае ошибки или если пользователь не захочет дальше что либо вводить)\n - немного расширил фильтр нецензурных слов\n - бот может ответить на любое сообщение в контексте которого присутствует слово 'бот'/'тупой'\n\n 🔸<code>Update v.0.0.2</code>\n- добавлена команда /getlocation (геопозицию можно передать через мобильное приложение telegram, ПК геопозицию не поддерживают)\n\n 🔸<code>Update v.0.0.3</code>\n- добавлена возможность администрирования бота, для этого необходимо быть администратором группы\n- добавлена панель администратора /apanel\n- команда /load теперь доступна только администраторам\n- добавлена команда /url - кнопки с сылками (в доработке)",parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands=['testp'])
async def cmd_test(message: types.Message):
    await message.answer(message.message_id)
    await message.answer(f'<b>{message.date}</b>',parse_mode=types.ParseMode.HTML)
    await message.answer(message.chat)
    await message.answer(message.from_user.full_name)
    
    
    
#@dp.message_handler(commands='dice')
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

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

@dp.message_handler(commands=['url'])
async def unload_from_database(message: types.Message):
    await message.answer(text='ссылки:',reply_markup=ikb_client)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_start,commands=['start','help'])
    dp.register_message_handler(cmd_dice,commands=['dice'])
    dp.register_message_handler(cmd_location,content_types=['location'])
    dp.register_message_handler(cmd_location_text,commands = ['getlocation'])
    