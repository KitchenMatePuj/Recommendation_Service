class IngredientsTransformer:
    @staticmethod
    def from_event(event: dict) -> dict:
        return {
            "ingredient_id": event.get("ingredient_id"),
            "recipe_id": event.get("recipe_id"),
            "name": event.get("name"),
            "measurement_unit": event.get("measurement_unit")
        }