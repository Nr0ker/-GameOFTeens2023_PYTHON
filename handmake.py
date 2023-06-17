from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from loader import dp, bot
from tarifs import TarifStatesGroup
from first_kb import *

@dp.callback_query_handler(text="hand_callback", state=TarifStatesGroup.handmade)
async def hand(message: types.Message, state: FSMContext):
    await bot.send_message(text="Добре тоді: ",
                           chat_id=message.from_user.id)
    photo = InputFile("photos/handmade_mock.png")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo)

    await bot.send_message(text="ХендМейд \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/",
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                               reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()