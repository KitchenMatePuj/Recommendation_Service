from src.main.python.repository.mongo_repository import find_recipes_by_filters

def get_recommendations(favorite_categories: list, allergies: list, cooking_time: int):
    return find_recipes_by_filters(
        categories=favorite_categories,
        allergies=allergies,
        max_cooking_time=cooking_time
    )
