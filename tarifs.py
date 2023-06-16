from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import asyncio

tarifs = ["ХендМейд", "Вільний лайф", "Смарт лайф", "Просто лайф", "Platinum Лайф", "Шкільний лайф", "Ґаджет", "Смарт сім'я", ["Роумінг Франція", "Роумінг Турція", "Роумінг Польша", "Роумінг Німечина"]]


class TarifStatesGroup(StatesGroup):
    rouming = State()
    handmade = State()
    family = State()
    unlimited_internet = State()
    unlimited_calls = State()


@dp.callback_query_handler(text='tariff_callback')
async def register_callback_function(message: types.Message):
    await message.answer("ABS")
    await TarifStatesGroup.rouming.set()
@dp.callback_query_handler(state=TarifStatesGroup.rouming)
async def register_callback_function(call: types.CallbackQuery,message: types.Message):
    await message.answer('Добре, для початку скажіть чи ви знаходитесь за кордоном?')
    await TarifStatesGroup.rouming.set()


@dp.callback_query_handler(state=TarifStatesGroup.rouming)
async def roaming_state_function(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Ок, ви хочете зробити свій тариф самі чи взяти вже готовий?')

    for i in range(8):
        tarifs.pop(i)
    print(tarifs)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text='no_callback')
async def register_callback_function(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Ок, ви хочете зробити свій тариф самі чи взяти вже готовий?')
    tarifs.pop(8)
    print(tarifs)

kb2 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Так', callback_data='yes_callback')],
        [types.InlineKeyboardButton(text='Ні', callback_data='no_callback')]
    ]
)

kb3 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Так', callback_data='yes_callback')],
        [types.InlineKeyboardButton(text='Ні', callback_data='no_callback')]
    ]
)
