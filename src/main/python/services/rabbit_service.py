from src.main.python.transformers.recipes_transformers import RecipesTransformer
from src.main.python.repository.mongo_repository import save_recipe_document

def process_recipe_event(message: dict):
    try:
        document = RecipesTransformer.from_event(message)
        save_recipe_document(document)
        print(f"[✓] Recipe processed and stored: {document.get('recipe_id')}")
    except Exception as e:
        print(f"[ERROR] Failed to process recipe event: {e}")
