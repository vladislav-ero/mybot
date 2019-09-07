from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_KEY = None

with open("token.txt") as f:
    API_KEY = f.read().strip()

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', 
level=logging.INFO, filename='bot.log')

def greet_user(bot, update):
    user_id = update.message.chat.id
    user_name = update.message.chat.username
    user_first_name = update.message.chat.first_name

    text = "Вызван /start, привет, сученыш"
    print(f"Message to {user_id} @{user_name} {user_first_name}: {text}")
    update.message.reply_text(text)
    second_text = "Напиши мне что-нибудь, ссыкло"
    update.message.reply_text(second_text)
    print(f"Message to {user_id} @{user_name} {user_first_name}: {second_text}")


def talk_to_me(bot, update):
    user_text = update.message.text
    user_id = update.message.chat.id
    user_first_name = update.message.chat.first_name
    # user_last_name = update.message.chat.last_name
    user_name = update.message.chat.username

    print(f"{user_id} @{user_name} {user_first_name}: {user_text}")
    user_text = user_text.lower()
    update.message.reply_text(f"Сам ты {user_text}, {user_first_name}")
    print(f"Response to {user_id} @{user_name} {user_first_name}:'Сам ты {user_text}, {user_first_name}'")

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()