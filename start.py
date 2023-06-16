import aiogram
from aiogram import *
from loader import dp
from first_kb import kb
import set_bot_commands


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer(f"Доброго дня, {message.from_user.full_name}!\n ", reply_markup=kb)


while True:
    bot_start(f"Доброго дня, {message.from_user.full_name}!\n ", reply_markup=kb)

