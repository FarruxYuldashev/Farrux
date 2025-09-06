import telebot
from telebot import types

TOKEN = "BOT_TOKENINGNI_QO'Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    webAppTest = types.WebAppInfo("https://SENING_WEB_APP_LINKING")  # Flutter web app linki
    markup.add(types.InlineKeyboardButton("Mini App ochish 🚀", web_app=webAppTest))
    bot.send_message(message.chat.id, "Salom! Mini appni oching 👇", reply_markup=markup)

bot.polling()
