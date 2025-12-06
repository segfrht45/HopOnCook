import telebot
from telebot import types

API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = telebot.TeleBot(API_TOKEN)

# Список доступних рецептів
RECIPES = {
    "Борщ": "1) Буряк\n2) Капуста\n3) Картопля\n4) М'ясо\nВарити приблизно 1 годину.",
    "Паста": "Паста, вершки, сир — перемішати та прогріти.",
    "Омлет": "Яйця, молоко, сіль — збити та смажити 5 хвилин."
}


def generate_menu():
    """Генерує клавіатуру зі списком страв."""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for dish in RECIPES:
        keyboard.add(dish)
    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привіт! Оберіть страву зі списку нижче ⬇️",
        reply_markup=generate_menu()
    )


@bot.message_handler(func=lambda message: True)
def send_recipe(message):
    dish = message.text.strip()
    if dish in RECIPES:
        bot.send_message(message.chat.id, f"📖 Рецепт «{dish}»:\n{RECIPES[dish]}")
    else:
        bot.send_message(message.chat.id, "❗ Будь ласка, виберіть страву зі списку.")


if name == "main":
    print("Бот запущено…")
    bot.infinity_polling()
