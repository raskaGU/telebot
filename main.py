import telebot
from telebot import types
import random
import os

bot = telebot.TeleBot("6967638915:AAE6k47pE5AHgzXFcE6Bx-A5rb4L1UFvCmw")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"))
    markup.add(types.KeyboardButton("Рандомный напиток"))
    markup.add(types.KeyboardButton("Рандомный стикер"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == "рандомный напиток")
def random_drink(message):
    drinks = ["Вода", "Кола", "Сок апельсиновый", "Фанта", "Чай"]
    random_drink = random.choice(drinks)
    bot.send_message(message.chat.id, f"Рандомный напиток: {random_drink}")

@bot.message_handler(func=lambda message: message.text.lower() == "рандомное число")
def random_number(message):
    random_number = random.randint(1, 100)
    bot.send_message(message.chat.id, f"Рандомное число: {random_number}")

sticker_dir = os.path.join(os.path.dirname(__file__), "images")

@bot.message_handler(func=lambda message: message.text.lower() == "рандомный стикер")
def random_sticker(message):
    stickers = os.listdir(sticker_dir)

    if not stickers:
        bot.send_message(message.chat.id, "В директории нет стикеров.")
        return

    random_sticker_path = os.path.join(sticker_dir, random.choice(stickers))
    with open(random_sticker_path, 'rb') as sticker_file:
        bot.send_sticker(message.chat.id, sticker_file)

bot.polling(none_stop=True)