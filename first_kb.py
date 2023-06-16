from aiogram import types

kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Підібрати тариф для вас', callback_data='tariff_callback')],
        [types.InlineKeyboardButton(text='Інші опції', callback_data='another_callback')]
    ]
)
