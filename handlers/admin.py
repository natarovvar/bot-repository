
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create import dp
from database import sqlite_database
from database.sqlite_database import sql_add_command


# класс состояний 
class FSMAdmin(StatesGroup): 
    photo = State()
    description = State()
    #price = State()
'''
class FSMGame(StatesGroup): 
    start = State()
'''
    
#@dp.message_handler(commands = 'load', state = None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('upload your photo (для отмены введите - /выход)')
    
# выход
# @dp.message_handler(state = "*", commands = 'выход')
# @dp.message_handler(Text(equals='отмена',ignore_case= True), state = "*")
async def exit_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer('Выход произведён')
    
#@dp.message_handler(content_types=['photo'], state = FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('description')

#@dp.message_handler(state = FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = (message.text)
    await sqlite_database.sql_add_command(state)
    await message.answer('Я записал данные')
    await state.finish()



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start,commands=['load'], state = None)
    dp.register_message_handler(exit_handler, state = "*", commands = 'выход')
    dp.register_message_handler(exit_handler, Text(equals='отмена',ignore_case= True ))
    dp.register_message_handler(load_photo,content_types=['photo'], state = FSMAdmin.photo)
    dp.register_message_handler(load_description, state = FSMAdmin.description)
   