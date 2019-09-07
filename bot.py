from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_KEY = ""

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', 
level=logging.INFO, filename='bot.log')

def greet_user(bot, update):
    text = "Вызван /start, привет, сученыш"
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    user_text = user_text.lower()
    update.message.reply_text(f"Сам ты {user_text}")

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()