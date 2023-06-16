from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN as TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
