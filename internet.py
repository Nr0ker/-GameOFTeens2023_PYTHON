from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from tarifs import TarifStatesGroup
from first_kb import kb_unlim_callOr_no, kb_calss


@dp.callback_query_handler(text="unlim_internet_callback", state=TarifStatesGroup.unlimited_internet)
async def unlim_choise_internet(message: types.Message):
    await bot.send_message(text="Наразі в нас є тільки лімітні дзівнки,вам підійдуть ці товари:", chat_id=message.from_user.id)
    list_of_photos = [InputFile("LifeTarifs/PlutinumLife.png"), InputFile("LifeTarifs/freeLife.png")]
    list_of_links1 = ["Вільний лайф: \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/",
                      "Платінум лайф \n  https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/"]
    num = 0
    while num != 2:
        num += 1
    for i in list_of_photos:
        await bot.send_photo(photo=i, chat_id=message.from_user.id)
    for links in list_of_links1:
        await bot.send_message(text=links, chat_id=message.from_user.id)

    await TarifStatesGroup.next()
