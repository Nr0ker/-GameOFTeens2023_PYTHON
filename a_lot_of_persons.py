from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from tarifs import TarifStatesGroup
from first_kb import kb_pupis


@dp.callback_query_handler(text="more_callback", state=TarifStatesGroup.pupils)
async def name_me(message: types.Message):
    await bot.send_message(text="На скільки людей потрібен тариф?", chat_id=message.from_user.id, reply_markup=kb_pupis)


@dp.callback_query_handler(text="fiveAndMore_people_callback")
async def fiveandmore(message: types.Message):
    await bot.send_message(text="Ось тарифи за вашим запитом:", chat_id=message.from_user.id)
    list_of_photos = [InputFile("LifeTarifs/smart_family.png"), InputFile("LifeTarifs/gaget.png")]
    list_of_links = ["Смарт сім'я \n https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/","Ґаджет \n https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/"]
    num = 0
    while num != 2:
        num += 1
    for i in list_of_photos:
        await bot.send_photo(photo=i, chat_id=message.from_user.id)
    for links in list_of_links:
        await bot.send_message(text=links, chat_id=message.from_user.id)


@dp.callback_query_handler(text="fiveAndLess_people_callback")
async def fiveandless(message: types.Message):
    await bot.send_message(text="Ось тарифи за вашим запитом:", chat_id=message.from_user.id)
    list_of_photos = [InputFile("LifeTarifs/smart_family.png"), InputFile("LifeTarifs/gaget.png"), InputFile("LifeTarifs/schoolLife.png")]
    list_of_links = ["Смарт сім'я \n https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/",
                     "Ґаджет \n https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/",
                     "Смарт сім'я \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/"]
    num = 0
    while num != 2:
        num += 1
    for i in list_of_photos:
        await bot.send_photo(photo=i, chat_id=message.from_user.id)
    for links in list_of_links:
        await bot.send_message(text=links, chat_id=message.from_user.id)



