from aiogram import types

kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Підібрати тариф для вас', callback_data='tariff_callback')],
        [types.InlineKeyboardButton(text='Інші опції', callback_data='another_callback')]
    ]
)


kb_yes_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Так', callback_data='yes_callback')],
        [types.InlineKeyboardButton(text='Ні', callback_data='no_callback')]
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
        [types.InlineKeyboardButton(text="З лімітом", callback_data='limit_internet_callback')]
    ]
)

kb_unlim_callOr_no = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Безліміт', callback_data='unlim_call_callback')],
        [types.InlineKeyboardButton(text="З лімітом", callback_data='limit_call_callback')]
    ]
)