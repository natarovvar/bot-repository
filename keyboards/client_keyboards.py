from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram import types


button1 = KeyboardButton('/dice')
button2 = KeyboardButton('test', web_app = True)
ibutton1 = InlineKeyboardButton(text='delete',url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
ibutton1 = InlineKeyboardButton(text='unload',url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
x = [InlineKeyboardButton(text='xabr',url='https://habr.com/ru/all/?ysclid=l6v8716gpv651661317')]

test_kb =  InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='download file',callback_data='file'))
delete_kb =  InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='❌',callback_data='delbutton'))


kb_client = ReplyKeyboardMarkup(resize_keyboard = True)
ikb_client = InlineKeyboardMarkup(row_width=2)
adb_admin = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='ADMINISTRATION PANEL',callback_data='dp'))
idb_client = InlineKeyboardMarkup(resize_keyboard = True).add(InlineKeyboardButton(text='delete',callback_data='del'),\
                                               InlineKeyboardButton(text='unload ',callback_data='uload'     ),\
                                                InlineKeyboardButton(text='load',callback_data='ld'))    

webi_kb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='<<>>', web_app=types.WebAppInfo(url="https://www.youtube.com/")),
                                                InlineKeyboardButton(text='game ',web_app=types.WebAppInfo(url="https://games.mihailgok.ru/")))
exit_adm = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='exit',callback_data='ex'))


kb_client.add(button1).add(button2)
ikb_client.row(*x)


