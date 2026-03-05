import telebot

TOKEN = "8795419190:AAHH23e2bpofjTi-dvarwKxI1uCt7vtREZU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Это Premium Shop бот.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
