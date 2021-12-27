import telebot
from telebot import types
import random
import os

bot = telebot.TeleBot('5049320818:AAGH4JtKkJt5RnP8zOW0rgfRWRlVAUFZ1E8')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Зима')
    item2 = types.KeyboardButton('Весна')
    item3 = types.KeyboardButton('Лето')
    item4 = types.KeyboardButton('Осень')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.from_user.id, 'Выбери кнопку', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == 'Зима':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Фото зима')
        item2 = types.KeyboardButton('Гиф зима')
        item3 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3)

        bot.send_message(message.from_user.id, 'Зима', reply_markup = markup)
    elif message.text == 'Весна':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Фото весна')
        item2 = types.KeyboardButton('Гиф весна')
        item3 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3)

        bot.send_message(message.from_user.id, 'Весна', reply_markup = markup)
    elif message.text == 'Лето':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Фото лето')
        item2 = types.KeyboardButton('Гиф лето')
        item3 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3)

        bot.send_message(message.from_user.id, 'Лето', reply_markup = markup)
    elif message.text == 'Осень':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Фото осень')
        item2 = types.KeyboardButton('Гиф осень')
        item3 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3)

        bot.send_message(message.from_user.id, 'Осень', reply_markup = markup)
    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Зима')
        item2 = types.KeyboardButton('Весна')
        item3 = types.KeyboardButton('Лето')
        item4 = types.KeyboardButton('Осень')
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.from_user.id, 'Выбери кнопку', reply_markup = markup)

bot.infinity_polling()