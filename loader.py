from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token="6159252007:AAEUYCdj_yjOfRKraxOfVH-aWReVH7d9mDA")
dp = Dispatcher(bot=bot, storage=MemoryStorage())
