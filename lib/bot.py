import telebot
from telebot import types

TOKEN = "7958495384:AAGxdSN3-oTv5QgO5mYaKgeYYPLXzwwOO-0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # Flutter Web app linkini shu yerga qo'yamiz
    webAppTest = types.WebAppInfo("https://demodversion.netlify.app/")
    markup.add(types.InlineKeyboardButton("Mini App ochish 🚀", web_app=webAppTest))
    bot.send_message(message.chat.id, "Salom! Mini appni oching 👇", reply_markup=markup)

bot.polling()

