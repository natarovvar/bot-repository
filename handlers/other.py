from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from create import dp
from aiogram.dispatcher.filters import Text
import json
import string

#@dp.message_handler()
async def cenz(message: types.Message):
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Артём сказал удалять такие сообщения!')
        await message.delete()

@dp.message_handler(lambda message: 'бот' in message.text)
async def i_am_robot(message: types.Message):
    await message.answer('Ты заикаешься? Бот – это ботва?')

@dp.message_handler(lambda message: 'бот' in message.text)
async def i_am_robot(message: types.Message):
    await message.answer('Ты заикаешься? Бот – это ботва?')

@dp.message_handler(lambda message: 'тупой' in message.text)
async def i_am_robot(message: types.Message):
    await message.answer('Сам такой!')
    await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(cenz)
    #dp.register_message_handler(i_am_robot,lambda message: 'бот' in message.text)

    