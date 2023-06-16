from aiogram import *
import aiogram
from loader import dp, bot


tarifs = ["Вільний лайф", "Смарт лайф", "Просто лайф", "Platinum Лайф", "Шкільний лайф", "Ґаджет", "Смарт сім'я"]


def money():
    @dp.message_handler()
    def handle_message(message):
        print(message.text)

        sent = bot.send_message(message.chat.id, "Максимальна ціна:")
        bot.register_next_step_handler(sent, save_link)

    def save_link(message):
        max_money = message.text

    @dp.message_handler()
    def handle_message(message):
        print(message.text)

        sent = bot.send_message(message.chat.id, "Мінімальна ціна:")
        bot.register_next_step_handler(sent, save_link)

    def save_link(message):
        min_money = message.text
