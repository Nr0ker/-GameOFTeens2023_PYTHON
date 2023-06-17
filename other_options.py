from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from first_kb import kb_rouming
from tarifs import TarifStatesGroup


@dp.callback_query_handler(text='another_callback')
async def another_option(message: types.Message):
    await bot.send_message(text='Виберіть тариф роумінгу який ви хочете вибрати:',
                           chat_id=message.from_user.id,
                           reply_markup=kb_rouming)



