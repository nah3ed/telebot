#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
# 6932742906:AAFjGOk003Ml6yBkpUnw4PhfTY20HfSaXW4
import telebot

API_TOKEN = '<6932742906:AAFjGOk003Ml6yBkpUnw4PhfTY20HfSaXW4>'

bot = telebot.TeleBot(6932742906:AAFjGOk003Ml6yBkpUnw4PhfTY20HfSaXW4)

# bot = telebot.TeleBot("6932742906:AAFjGOk003Ml6yBkpUnw4PhfTY20HfSaXW4", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
# @bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
# def send_welcome(message):bot.reply_to(message, "Howdy, how are you doing?")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)

# @bot.message_handler(func=lambda m: True)

def echo_message(message):
    bot.reply_to(message, message.text)

#def echo_all(message):bot.reply_to(message, message.text)




bot.infinity_polling()
