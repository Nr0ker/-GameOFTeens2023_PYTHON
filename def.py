from aiogram import *
import aiogram
import telebot

tarifs = ["Вільний лайф", "Смарт лайф", "Просто лайф", "Platinum Лайф", "Шкільний лайф", "Ґаджет", "Смарт сім'я"]
def money():
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        print(message.text)

        sent = bot.send_message(message.chat.id, "Максимальна ціна:")
        bot.register_next_step_handler(sent, save_link)

    def save_link(message):
        my_link = message.text
