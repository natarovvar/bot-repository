
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram import types, md
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create import dp, bot
from database import sqlite_database
from database.sqlite_database import sql_add_command
import database

from keyboards import kb_client,ikb_client,idb_client

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

ID = None

# класс состояний 
class FSMAdmin(StatesGroup): 
    photo = State()
    description = State()
    #price = State()
'''
class FSMGame(StatesGroup): 
    start = State()
'''
@dp.message_handler(commands=['apanel'],is_chat_admin = True) 
async def administration_panel(message: types.Message):
    global ID,aname,date
    ID = message.from_user.id
    aname = message.from_user.full_name
    adate = message.date
    await bot.send_message(message.from_user.id, f'the admin panel is activated🟢\nWelcome! <b>{aname}</b>\nlogin at: {adate}\n\nuse /p to call the panel',parse_mode=types.ParseMode.HTML)
    await message.delete()
  
    
    
#@dp.message_handler(commands = 'load', state = None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('upload your photo (для отмены введите - /e)')
    
# выход
# @dp.message_handler(state = "*", commands = '/e')
# @dp.message_handler(Text(equals='отмена',ignore_case= True), state = "*")
async def exit_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer('Выход произведён')
    
#@dp.message_handler(content_types=['photo'], state = FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('description')

#@dp.message_handler(state = FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = (message.text)
        await sqlite_database.sql_add_command(state)
        await message.answer('Я записал данные')
        await state.finish()

    
@dp.message_handler(commands=['p'])
async def database_cmd(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id,text=f'<code>administation panel</code>',reply_markup=idb_client,parse_mode=types.ParseMode.HTML)

    

@dp.callback_query_handler(text='del')
async def dell_call(callback: types.CallbackQuery):
    await callback.message.answer('Данные удалены')
    await callback.answer()
    
@dp.callback_query_handler(text='ld')
async def cm_start_inlinekeyboards(callback: types.CallbackQuery, state = None):
    if callback.from_user.id == ID:
        await FSMAdmin.photo.set()
        await callback.message.answer('upload your photo (для отмены введите - /e)')   

@dp.callback_query_handler(text='uload')
async def uload_inkeyboard(call: types.CallbackQuery):
    await sqlite_database.sql_unload(call)
    



    



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start,commands=['load'], state = None)
    dp.register_message_handler(exit_handler, state = "*", commands = 'e')
    dp.register_message_handler(exit_handler, Text(equals='отмена',ignore_case= True ))
    dp.register_message_handler(load_photo,content_types=['photo','document'], state = FSMAdmin.photo)
    dp.register_message_handler(load_description, state = FSMAdmin.description)
   