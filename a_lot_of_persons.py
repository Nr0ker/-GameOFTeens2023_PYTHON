from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from tarifs import TarifStatesGroup
from first_kb import *



@dp.callback_query_handler(text='more_callback', state=TarifStatesGroup.pupils)
async def name_me(message: types.Message):
    await bot.send_message(text="На скільки людей потрібен тариф?", chat_id=message.from_user.id, reply_markup=kb_pupis)


@dp.callback_query_handler(text='fiveAndMore_people_callback', state=TarifStatesGroup.pupils)
async def fiveandmore(message: types.Message):
    photo1 = InputFile("LifeTarifs/smart_family.png")
    photo2 = InputFile("LifeTarifs/gaget.png")
    await bot.send_message(text="Ось тарифи за вашим запитом:", chat_id=message.from_user.id)
    await bot.send_photo(photo=photo1,
                           chat_id=message.from_user.id)
    await bot.send_message(text="Смарт сім'я \n https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/",
                           chat_id=message.from_user.id)
    await bot.send_photo(photo=photo2,
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ґаджет \n https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/",
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id, reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()

@dp.callback_query_handler(text='fiveAndLess_people_callback', state=TarifStatesGroup.pupils)
async def fiveandless(message: types.Message):
    photo1 = InputFile("LifeTarifs/smart_family.png")
    photo2 = InputFile("LifeTarifs/gaget.png")
    photo3 = InputFile("LifeTarifs/schoolLife.png")
    await bot.send_message(text="Ось тарифи за вашим запитом:", chat_id=message.from_user.id)
    await bot.send_photo(photo=photo1,
                         chat_id=message.from_user.id)
    await bot.send_message(text="Смарт сім'я \n https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/",
                           chat_id=message.from_user.id)
    await bot.send_photo(photo=photo2,
                         chat_id=message.from_user.id)
    await bot.send_message(text="Ґаджет \n https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/",
                           chat_id=message.from_user.id)
    await bot.send_photo(photo=photo3,
                         chat_id=message.from_user.id)
    await bot.send_message(text="Шкільний \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/",
                           chat_id=message.from_user.id)
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                               reply_markup=kb_finish)

    await TarifStatesGroup.finish.set()
