from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from tarifs import TarifStatesGroup
from first_kb import kb_unlim_callOr_no2, kb_calss


@dp.callback_query_handler(text="unlim_internet_callback", state=TarifStatesGroup.unlimited_internet)
async def unlim_choise_internet(message: types.Message):
    await bot.send_message(text='Дзвінки безлімітні чи ні?', chat_id=message.from_user.id,
                           reply_markup=kb_unlim_callOr_no2)


@dp.callback_query_handler(text='unlim_call_callback')
async def unlim_internet(message: types.Message):
    await bot.send_message(text="наразі немає таких товарів, але можемо запропонувати вам інший", chat_id=message.from_user.id, reply_markup=kb_calss)


@dp.callback_query_handler(text="limit_call_callback")
async def limited_internet(message: types.Message):
    await bot.send_message(text="Тоді виберіть кількість хвилин", chat_id=message.from_user.id, reply_markup=kb_calss)


@dp.callback_query_handler(text="2000min_callback")
async def min_internet(message: types.Message):
    photo = InputFile("LifeTarifs/freeLife.png")
    await bot.send_photo(photo=photo, chat_id=message.from_user.id)
    await bot.send_message(text="Ось тариф по вашому запиту та силка на нього: \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/", chat_id=message.from_user.id)


@dp.callback_query_handler(text="2000max_callback")
async def max_internet(message: types.Message):
    photo = InputFile("LifeTarifs/PlutinumLife.png")
    await bot.send_photo(photo=photo, chat_id=message.from_user.id)
    await bot.send_message(
        text="Ось тариф по вашому запиту та силка на нього: \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/",
        chat_id=message.from_user.id)
