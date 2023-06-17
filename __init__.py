from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
import internet
from first_kb import set_default_commands
import tarifs
from aiogram import executor, types
import a_lot_of_persons
import aiogram
from aiogram.types import *
import handmake
import rouming
from loader import dp, bot
from set_bot_commands import set_default_commands
from first_kb import kb


@dp.message_handler(commands=['clear'])

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer(f"Слава Україні!!!")
    await message.answer(f"Привіт, {message.from_user.full_name}!\n ", reply_markup=kb)

    # photo = InputFile("photos/Гаджет.png")
    # await bot.send_photo(chat_id= message.chat.id, photo=photo)

@dp.message_handler(commands=["stop"])
async def stop_command(message: types.Message, state: FSMContext):
    await message.reply("Выключение бота...")
    # Остановка бота
    await dp.stop_polling()
    await bot.close()


@dp.message_handler(commands=['help'])
async def bot_help(message: types.Message):
    await message.answer("\nСписок команд: \n/start - Почати діалог\n/help - Отримати поміч\n stop- Зупинити бота")


executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


