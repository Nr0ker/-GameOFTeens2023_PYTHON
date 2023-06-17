from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Отримати допомогу"),
        ]
    )


kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Підібрати тариф для вас', callback_data='tariff_callback')]
    ]
)


kb_yes_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Так,за кордоном', callback_data='rouming_callback')],
        [types.InlineKeyboardButton(text='Ні, в Україні', callback_data='ukr_callback')]

    ]
)

kb_handOr_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Вручну', callback_data='hand_callback')],
        [types.InlineKeyboardButton(text='Готовий', callback_data='ready_callback')]

    ]
)


kb_oneOr_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Одна', callback_data='one_callback')],
        [types.InlineKeyboardButton(text="Більше", callback_data='more_callback')]

    ]
)

kb_unlim_internetOr_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Безліміт', callback_data='unlim_internet_callback')],
        [types.InlineKeyboardButton(text="З лімітом", callback_data='limit_internet_callback')],

    ]
)



kb_unlim_callOr_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Безліміт', callback_data='unlim_call_callback')],
        [types.InlineKeyboardButton(text="З лімітом", callback_data='limit_call_callback')],

    ]
)

kb_unlim_callOr_no2 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Безліміт', callback_data='unlim_call_callback')],
        [types.InlineKeyboardButton(text="З лімітом", callback_data='limit_call_callback')],

    ]
)



kb_rouming = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Франція роумінг', callback_data='France_call_callback')],
        [types.InlineKeyboardButton(text="Турція роумінг", callback_data='Turcia_call_callback')],
        [types.InlineKeyboardButton(text='Польша роумінг', callback_data='Polsha_call_callback')],
        [types.InlineKeyboardButton(text="Німетчина роумінг", callback_data='Nimetchina_call_callback')],
        [types.InlineKeyboardButton(text="Італія роумінг", callback_data='Italy_call_callback')]


    ]
)

kb_pupis = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="5 і більше", callback_data='fiveAndMore_people_callback')],
        [types.InlineKeyboardButton(text="5 і меньше", callback_data='fiveAndLess_people_callback')]

    ]
)

kb_finish = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="Ні", callback_data='No_fin_callback')],
        [types.InlineKeyboardButton(text="Так", callback_data='yes_fin_callback')]

    ]
)

kb_calss = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="2000 і меньше хвилин", callback_data='2000min_callback')],
        [types.InlineKeyboardButton(text="2000 і більше", callback_data='2000max_callback')]

    ]
)
