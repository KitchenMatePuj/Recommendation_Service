class RecipesTransformer:
    @staticmethod
    def from_event(event: dict) -> dict:
        return {
            "recipe_id": event.get("recipe_id"),
            "title": event.get("title"),
            "keycloak_user_id": event.get("keycloak_user_id"),
            "cooking_time": event.get("cooking_time"),
            "rating_avg": event.get("rating_avg"),
            "categories": event.get("categories", [])
        }