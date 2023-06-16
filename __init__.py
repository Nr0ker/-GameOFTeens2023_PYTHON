from aiogram import executor
import loader
from set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

executor.start_polling(loader.dp, on_startup=on_startup, skip_updates=True)
