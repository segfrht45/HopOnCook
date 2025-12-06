def get_recipe(recipe_name):
    if not recipe_name:
        return "Please provide a recipe name."
    return f"Recipe for {recipe_name} is not ready yet."

if name == "main":
    print(get_recipe("Borsh"))
