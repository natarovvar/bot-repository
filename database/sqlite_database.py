
from email.mime import message
from os import curdir
import sqlite3 as sq

from keyboards.client_keyboards import delete_kb,exit_adm

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from aiogram import types, md
from aiogram import Dispatcher
from create import dp, bot



def sql_database_start():
    global base,cur
    base = sq.connect('paperclip_database.db')
    cur = base.cursor()
    if base:
        print('data base is connected')
    base.execute('CREATE TABLE IF NOT EXISTS loaded(img TEXT, description TEXT )')
    base.execute('CREATE TABLE IF NOT EXISTS geoposition(user TEXT, latitude TEXT, longitude TEXT, address TEXT)')
    base.commit()
    
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO loaded VALUES (?,?)', tuple(data.values()))
        base.commit()

async def sql_add_geopostition(username, lat, lon, address):
        cur.execute('INSERT INTO geoposition VALUES (?,?,?,?)', (username, lat, lon, address))
        base.commit()

"""
@dp.callback_query_handler(text='uload')
async def del_uload(call: types.CallbackQuery):
    for res in cur.execute('SELECT * FROM loaded').fetchall():
        await bot.send_photo(call.from_user.id,res[0])
  """      

      
async def sql_unload(call: types.CallbackQuery):
    for res in cur.execute('SELECT * FROM loaded').fetchall():
        await bot.send_photo(call.from_user.id,res[0],f'{res[1]}')
        #await call.message.answer(text='>>>',reply_markup=delete_kb)
        await call.message.answer(text='>>>',reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(f'❌ {res[1]}',callback_data = f'del {res[1]}')))
    await call.answer()

"""async def sql_delete_description(description_text):
    cur.execute(f"DELETE FROM loaded WHERE description = '{description_text}'")
    base.commit()
    """
        
     
 




        
        