from src.main.python.repository.mongo_repository import (
    save_recipe_document,
    update_recipe_document,
    delete_recipe_document,
    add_ingredient_to_recipe,
    update_ingredient_in_recipe,
    delete_ingredient_from_recipe
)
from src.main.python.transformers.recipes_transformers import RecipesTransformer
from src.main.python.transformers.ingredients_transformers import IngredientsTransformer


def process_recipe_event(message: dict):
    try:
        event_type = message.get("event")

        if event_type in ["recipe_created", "recipe_updated"]:
            document = RecipesTransformer.from_event(message)
            if event_type == "recipe_created":
                save_recipe_document(document)
            else:
                update_recipe_document(document)

        elif event_type == "recipe_deleted":
            recipe_id = message.get("recipe_id")
            delete_recipe_document(recipe_id)

        elif event_type in ["ingredient_created", "ingredient_updated", "ingredient_deleted"]:
            recipe_id = message.get("recipe_id")
            ingredient = IngredientsTransformer.from_event(message)

            if event_type == "ingredient_created":
                add_ingredient_to_recipe(recipe_id, ingredient)
            elif event_type == "ingredient_updated":
                update_ingredient_in_recipe(recipe_id, ingredient)
            elif event_type == "ingredient_deleted":
                delete_ingredient_from_recipe(recipe_id, ingredient["name"])

        print(f"[✓] Event processed: {event_type}")

    except Exception as e:
        print(f"[ERROR] Failed to process recipe event: {e}")

