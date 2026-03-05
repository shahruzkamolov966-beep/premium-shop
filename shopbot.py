import telebot
from telebot import types

TOKEN = "ВСТАВЬ_СЮДА_НОВЫЙ_ТОКЕН"
ADMIN_ID = 8408049611

bot = telebot.TeleBot(TOKEN)

# СТАРТ
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛒 Купить", "📞 Поддержка")

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Premium Shop 💎",
        reply_markup=markup
    )


# ПОДДЕРЖКА
@bot.message_handler(func=lambda message: message.text == "📞 Поддержка")
def support(message):
    bot.send_message(
        message.chat.id,
        "Напишите в поддержку: @Premium_shop_telegram_bot"
    )


# МАГАЗИН
@bot.message_handler(func=lambda message: message.text == "🛒 Купить")
def shop(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💎 Telegram Premium")
    markup.add("⭐ Telegram Stars")
    markup.add("🎮 Robux")
    markup.add("🧠 Brainrot")
    markup.add("⬅️ Назад")

    bot.send_message(
        message.chat.id,
        "Выберите товар:",
        reply_markup=markup
    )


# НАЗАД
@bot.message_handler(func=lambda message: message.text == "⬅️ Назад")
def back(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛒 Купить", "📞 Поддержка")

    bot.send_message(
        message.chat.id,
        "Главное меню",
        reply_markup=markup
    )


# TELEGRAM PREMIUM
@bot.message_handler(func=lambda message: message.text == "💎 Telegram Premium")
def premium(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Купить 1 месяц", callback_data="premium_1"))
    markup.add(types.InlineKeyboardButton("Купить 3 месяца", callback_data="premium_3"))
    markup.add(types.InlineKeyboardButton("Купить 1 год", callback_data="premium_12"))

    text = """📦 Telegram Premium

1 месяц — 60 000 сум
3 месяца — 150 000 сум
1 год — 330 000 сум
"""

    bot.send_message(message.chat.id, text, reply_markup=markup)


# TELEGRAM STARS
@bot.message_handler(func=lambda message: message.text == "⭐ Telegram Stars")
def stars(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Купить 100", callback_data="stars_100"))
    markup.add(types.InlineKeyboardButton("Купить 200", callback_data="stars_200"))
    markup.add(types.InlineKeyboardButton("Купить 500", callback_data="stars_500"))
    markup.add(types.InlineKeyboardButton("Купить 1000", callback_data="stars_1000"))

    text = """⭐ Telegram Stars

100 — 28 000 сум
200 — 56 000 сум
500 — 120 000 сум
1000 — 250 000 сум
"""

    bot.send_message(message.chat.id, text, reply_markup=markup)


# ROBUX
@bot.message_handler(func=lambda message: message.text == "🎮 Robux")
def robux(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Купить 80", callback_data="robux_80"))
    markup.add(types.InlineKeyboardButton("Купить 160", callback_data="robux_160"))
    markup.add(types.InlineKeyboardButton("Купить 400", callback_data="robux_400"))
    markup.add(types.InlineKeyboardButton("Купить 800", callback_data="robux_800"))

    text = """🎮 Robux

80 — 15 000 сум
160 — 30 000 сум
400 — 75 000 сум
800 — 150 000 сум
"""

    bot.send_message(message.chat.id, text, reply_markup=markup)


# BRAINROT
@bot.message_handler(func=lambda message: message.text == "🧠 Brainrot")
def brainrot(message):

    bot.send_message(
        message.chat.id,
        "Для покупки Brainrot напишите в ЛС: @Premium_shop_telegram_bot"
    )


# ЗАКАЗ
@bot.callback_query_handler(func=lambda call: True)
def order(call):

    bot.send_message(call.message.chat.id, "✅ Заказ отправлен!")

    username = call.from_user.username
    if username is None:
        username = "без_username"

    bot.send_message(
        ADMIN_ID,
        f"""📦 Новый заказ

Пользователь: @{username}
ID: {call.from_user.id}

Товар: {call.data}
"""
    )


bot.infinity_polling()
web = types.WebAppInfo("https://premiumshop.netlify.app")
