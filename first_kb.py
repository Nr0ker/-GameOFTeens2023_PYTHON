from aiogram import types

kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Тариф', callback_data='tarif_callback')],
        [types.InlineKeyboardButton(text='Інші опції', callback_data='another_callback')]
    ]
)
