from Game_of_Teens1 import tarifs
from aiogram import executor, types
import aiogram
from aiogram.types import *

from loader import dp, bot
from set_bot_commands import set_default_commands
from first_kb import kb



@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer(f"Доброго дня, {message.from_user.full_name}!\n ", reply_markup=kb)

    # photo = InputFile("photos/Гаджет.png")
    # await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(commands=['help'])
async def bot_help(message: types.Message):
    await message.answer("\nСписок команд: \n/start - Почати діалог\n/help - Отримати поміч")


executor.start_polling(dp, skip_updates=True)
