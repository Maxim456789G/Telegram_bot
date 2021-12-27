import telebot
from telebot import types

bot = telebot.TeleBot('5049320818:AAGH4JtKkJt5RnP8zOW0rgfRWRlVAUFZ1E8')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item = types.KeyboardButton('👍Лето👍')
    item1 = types.KeyboardButton('✋Зима✋')
    item2 = types.KeyboardButton('🖐Весна🖐')
    item4 = types.KeyboardButton('1')
    item5 = types.KeyboardButton('2')
    item6 = types.KeyboardButton('3')
    item7 = types.KeyboardButton('4')
    item8 = types.KeyboardButton('6')
    item9 = types.KeyboardButton('7')
    item10 = types.KeyboardButton('8')
    item11 = types.KeyboardButton('9')
    markup.add(item, item1, item2, item4, item5, item6, item7, item8, item9, item10, item11)
    bot.send_message(message.from_user.id, 'Выбери кнопку', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def get_text_messager(message):
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет мой друг!')
    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')
    elif message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'ничего')
    elif message.text == 'как погода?':
        bot.send_message(message.from_user.id, 'солнечная погода')
    else:
        bot.send_message(message.from_user.id, 'Прости я тебя не понял')

bot.infinity_polling()
