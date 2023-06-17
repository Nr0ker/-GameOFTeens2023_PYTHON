from aiogram.types import InputFile
from loader import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from first_kb import *
import time

tarifs = ["ХендМейд", "Вільний лайф", "Смарт лайф", "Просто лайф", "Platinum Лайф", "Шкільний лайф", "Ґаджет",
          "Смарт сім'я", "Роумінг"]


# Стейти - Етапи
class TarifStatesGroup(StatesGroup):
    handmade = State()
    rouming = State()
    pupils = State()
    unlimited_internet = State()
    unlimited_calls = State()
    finish = State()




# Питання
@dp.callback_query_handler(text="tariff_callback")
async def chose_ready_or_hand_func(message: types.Message):
    await message.answer("Почнемо!")
    await bot.send_message(text='Ви хочете зробити свій тариф самі чи взяти вже готовий?',
                           chat_id=message.from_user.id,
                           reply_markup=kb_handOr_no)
    await TarifStatesGroup.handmade.set()


@dp.callback_query_handler(text='ready_callback', state=TarifStatesGroup.handmade)
async def chose_rouming_func(message: types.Message):
    await bot.send_message(text='Зараз скажіть чи ви знаходитесь за кордоном?',
                           chat_id=message.from_user.id, reply_markup=kb_yes_no)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text='ukr_callback', state=TarifStatesGroup.rouming)
async def chose_pupils_func(message: types.Message):
    await bot.send_message(text="Тариф для 1 людини чи більше?", chat_id=message.from_user.id, reply_markup=kb_oneOr_no)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text='one_callback', state=TarifStatesGroup.pupils)
async def chose_internet_func(message: types.Message):
    await bot.send_message(text='Інтернет безлімітний чи ні?', chat_id=message.from_user.id,
                           reply_markup=kb_unlim_internetOr_no)
    await TarifStatesGroup.next()


@dp.callback_query_handler(text="unlim_internet_callback", state=TarifStatesGroup.unlimited_internet)
async def unlim_choise_internet(message: types.Message):
    await bot.send_message(text='Дзвінки безлімітні чи ні?', chat_id=message.from_user.id,
                           reply_markup=kb_unlim_callOr_no)


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


@dp.callback_query_handler(text='limit_internet_callback', state=TarifStatesGroup.unlimited_internet)
async def chose_call_func(message: types.Message):
    await bot.send_message(text='Дзвінки безлімітні чи ні?', chat_id=message.from_user.id,
                           reply_markup=kb_unlim_callOr_no)
    await TarifStatesGroup.next()

@dp.callback_query_handler(text="unlim_call_callback", state=TarifStatesGroup.unlimited_calls)
async def unlim_call(message: types.Message):
    photo = InputFile("LifeTarifs/schoolLife.png")
    await bot.send_photo(photo=photo, chat_id=message.from_user.id)
    await bot.send_message(text="Ось наш товар для вас: \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/", chat_id=message.from_user.id)

@dp.callback_query_handler(text='limit_call_callback', state=TarifStatesGroup.unlimited_calls)
async def inlim_calls(message: types.Message):
    await bot.send_message(text="Тоді вам підійдуть ці товари:", chat_id=message.from_user.id)
    list_of_photos = [InputFile("LifeTarifs/simpleLife.png"), InputFile("LifeTarifs/smartLife.png")]
    list_of_links1 = ["Смарт лайф \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/",
                      "Просто лайф \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/"]
    num = 0
    while num != 2:
        num += 1
    for i in list_of_photos:
        await bot.send_photo(photo=i, chat_id=message.from_user.id)
    for links in list_of_links1:
        await bot.send_message(text=links, chat_id=message.from_user.id)
    
    await bot.send_message(text="Ви хочете вибрати ще інший таріф?", chat_id=message.from_user.id,
                           reply_markup=kb_finish)
    await TarifStatesGroup.finish.set()



@dp.callback_query_handler(text='No_fin_callback', state=TarifStatesGroup.finish)
async def fin_No(message: types.Message):
    await bot.send_message(text="Добре до побачення! Дякую за користування! :)", chat_id=message.from_user.id)
    await message.reply("Напишіть /start що б почати...")
    await dp.stop_polling()
    await bot.close()

@dp.callback_query_handler(text='yes_fin_callback', state=TarifStatesGroup.finish)
async def fin_Yes(message: types.Message, state: FSMContext):
    await bot.send_message(text="Добре!", chat_id=message.from_user.id)
    await bot.send_message(text=f"Продовжуємо, {message.from_user.full_name}!\n ", chat_id=message.from_user.id , reply_markup=kb)
    await state.reset_state()
