import telebot
from telebot import types

API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = telebot.TeleBot(API_TOKEN)

RECIPES = {
    "Борщ": "🟥 Буряк\n🥬 Капуста\n🥔 Картопля\n🍖 М'ясо\n⏱ Варити близько 1 години.",
    "Паста": "🍝 Паста, вершки, сир — перемішати та прогріти.",
    "Омлет": "🍳 Яйця, молоко, сіль — збити та смажити 5 хвилин."
}


def generate_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for dish in RECIPES:
        keyboard.add(dish)
    return keyboard


def get_recipe_text(dish: str) -> str:
    """Повертає текст рецепта."""
    if dish not in RECIPES:
        return "😔 Цієї страви немає у списку. Оберіть з меню нижче."
    return f"📖 Рецепт «{dish}»:\n{RECIPES[dish]}"


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привіт! Оберіть страву зі списку нижче ⬇️",
        reply_markup=generate_menu()
    )


@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    dish = message.text.strip()
    response = get_recipe_text(dish)
    bot.send_message(message.chat.id, response)


if name == "main":
    print("Бот запущено…")
    bot.infinity_polling()
