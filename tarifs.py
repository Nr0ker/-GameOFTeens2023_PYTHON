from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import asyncio
from first_kb import kb_yes_no, kb_handOr_no, kb_oneOr_no, kb_unlim_internetOr_no, kb_unlim_callOr_no
tarifs = ["ХендМейд", "Вільний лайф", "Смарт лайф", "Просто лайф", "Platinum Лайф", "Шкільний лайф", "Ґаджет", "Смарт сім'я", ["Роумінг Франція", "Роумінг Турція", "Роумінг Польша", "Роумінг Німечина"]]



class TarifStatesGroup(StatesGroup):
    handmade = State()
    rouming = State()
    family = State()
    unlimited_internet = State()
    unlimited_calls = State()

@dp.callback_query_handler(text="tariff_callback")
async def a(message: types.Message, state: FSMContext):
    await message.answer("Почнемо!")
    await bot.send_message(text='Зараз скажіть чи ви знаходитесь за кордоном?', chat_id=message.from_user.id,
                           reply_markup=kb_yes_no)
    await TarifStatesGroup.handmade.set()
@dp.callback_query_handler(text='no_callback', state=TarifStatesGroup.rouming)
async def register_callback_function(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(text='Добре, ви хочете зробити свій тариф самі чи взяти вже готовий?',
                           chat_id=call.from_user.id,
                           reply_markup=kb_handOr_no)  # Он сначала должен выбрать вручную или готовий!
    await TarifStatesGroup.next()
@dp.callback_query_handler(text="ready_callback", state=TarifStatesGroup.handmade)
async def roaming_state_function(call: types.CallbackQuery,  state: FSMContext):
    await bot.send_message(text='Тариф для 1 людини чи більше?', chat_id=call.from_user.id, reply_markup=kb_oneOr_no)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text='one_callback', state=TarifStatesGroup.family)
async def register_callback_function(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message('Інтернет безлімітний чи ні?', chat_id=call.from_user.id, reply_markup=kb_unlim_internetOr_no)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text='limit_internet_callback', state=TarifStatesGroup.unlimited_internet)
async def register_callback_function(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message('Дзвінки безлімітні чи ні?', chat_id=call.from_user.id, reply_markup=kb_unlim_callOr_no)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text='limit_call_callback', state=TarifStatesGroup.unlimited_calls)
async def register_callback_function(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message('Дзвінки безлімітні чи ні?', chat_id=call.from_user.id, reply_markup=kb_unlim_callOr_no)
    await bot.send_message('Це все покищо', chat_id=call.from_user.id)


