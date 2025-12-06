import telebot

API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = telebot.TeleBot(API_TOKEN)

# Невелика база рецептів
RECIPES = {
    "борщ": "1) Буряк\n2) Капуста\n3) Картопля\n4) М'ясо\nВарити приблизно 1 годину.",
    "паста": "Паста, вершки, сир — перемішати та прогріти.",
    "омлет": "Яйця, молоко, сіль — збити та смажити 5 хвилин."
}


def get_recipe(recipe_name: str) -> str:
    """
    Повертає рецепт за назвою страви.
    """
    if not recipe_name:
        return "❗ Будь ласка, вкажіть назву страви."

    recipe_name = recipe_name.lower()

    if recipe_name in RECIPES:
        return f"📖 Рецепт «{recipe_name}»:\n{RECIPES[recipe_name]}"

    return "😔 На жаль, такого рецепта поки немає."


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привіт! Я бот з рецептами.\n"
        "Напишіть назву страви — і я надішлю рецепт!"
    )


@bot.message_handler(func=lambda msg: True)
def handle_recipe_request(message):
    recipe_name = message.text.strip()
    response = get_recipe(recipe_name)
    bot.send_message(message.chat.id, response)


if name == "main":
    print("Бот запущено...")
    bot.infinity_polling()
