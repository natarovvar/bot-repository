
from aiogram import Bot, Dispatcher
import os 
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token = os.getenv('TOKEN')) # объект бота
channel_id = os.getenv('CHANNEL_ID')
dp = Dispatcher(bot, storage = storage) # объект диспетчера