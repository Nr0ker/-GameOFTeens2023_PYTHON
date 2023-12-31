from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from first_kb import *
from tarifs import TarifStatesGroup
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text='rouming_callback', state=TarifStatesGroup.rouming)
async def rouming(message: types.Message):
    await bot.send_message(text='Виберіть тариф роумінгу який ви хочете вибрати:',
                           chat_id=message.from_user.id,
                           reply_markup=kb_rouming)





@dp.callback_query_handler(text='France_call_callback', state=TarifStatesGroup.rouming)
async def fr(message: types.Message, state: FSMContext):
    await bot.send_message(text='Тоді для вас підійде - роумінг Франція:',
                           chat_id=message.from_user.id)
    photo = InputFile("photos/france.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo1 = InputFile("photos/Franc_Description.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1)
    await bot.send_message(text='https://www.lifecell.ua/uk/mobilnij-zvyazok/roaming/bazovi-tarifi-v-roumingu/',
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                               reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()

@dp.callback_query_handler(text='Turcia_call_callback', state=TarifStatesGroup.rouming)
async def tr(message: types.Message, state: FSMContext):
    await bot.send_message(text='Тоді для вас підійде - роумінг Турція:',
                           chat_id=message.from_user.id)
    photo = InputFile("photos/turcia.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo1 = InputFile("photos/Türkiye.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1)
    await bot.send_message(text='https://www.lifecell.ua/uk/mobilnij-zvyazok/roaming/bazovi-tarifi-v-roumingu/',
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                               reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()

@dp.callback_query_handler(text='Polsha_call_callback', state=TarifStatesGroup.rouming)
async def pl(message: types.Message, state: FSMContext):
    await bot.send_message(text='Тоді для вас підійде - роумінг Польша:',
                           chat_id=message.from_user.id)
    photo = InputFile("photos/polsha.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo1 = InputFile("photos/Poland.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1)
    await bot.send_message(text='https://www.lifecell.ua/uk/mobilnij-zvyazok/roaming/bazovi-tarifi-v-roumingu/',
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                               reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()

@dp.callback_query_handler(text='Nimetchina_call_callback', state=TarifStatesGroup.rouming)
async def nim(message: types.Message, state: FSMContext):
    await bot.send_message(text='Тоді для вас підійде - роумінг Німеччина:',
                           chat_id=message.from_user.id)
    photo = InputFile("photos/NIMETCHINA.jpeg")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo1 = InputFile("photos/Germany.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1)
    await bot.send_message(text='https://www.lifecell.ua/uk/mobilnij-zvyazok/roaming/bazovi-tarifi-v-roumingu/',
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                               reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()

@dp.callback_query_handler(text='Italy_call_callback', state=TarifStatesGroup.rouming)
async def italy(message: types.Message, state: FSMContext):
    await bot.send_message(text='Тоді для вас підійде - роумінг Італія:',
                           chat_id=message.from_user.id)
    photo = InputFile("photos/italy.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo1 = InputFile("photos/Italy_2.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1)
    await bot.send_message(text='https://www.lifecell.ua/uk/mobilnij-zvyazok/roaming/bazovi-tarifi-v-roumingu/',
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id, reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()