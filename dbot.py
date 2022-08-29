
from aiogram.utils import executor
from create import dp
from database import sqlite_database



async def on_startup(_):
    print("bot online")
    sqlite_database.sql_database_start()

from handlers import client
from handlers import admin
from handlers import other



client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
    
