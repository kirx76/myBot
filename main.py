import os

import telebot
from dotenv import load_dotenv

from functions import *

functions = [
    generate_function_description('start', 'Just a start Function'),
    generate_function_description('help', 'Use it if forgot functions'),
]


def my_bot():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.from_user.id,
                         "Hi, i'm now just a voter bot.\nIn next days i'm be able to "
                         "show your lovely model.\nJust wait it :)")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.from_user.id, get_all_functions(function_list=functions, is_text=True))

    bot.polling()


if __name__ == '__main__':
    info('Loading env file')
    load_dotenv()
    info('Loading env file complete')
    info('Initialize bot')
    bot = telebot.TeleBot(os.getenv('token'), parse_mode=None)
    info('Initialize complete, now you can use the bot')
    my_bot()
