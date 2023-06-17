from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="unlim_call_callback")
async def unlim_call(message: types.Message):
    pass