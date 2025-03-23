from typing import List, Optional
from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    keycloak_user_id: str
    favorite_categories: List[str]
    allergies: List[str]
    cooking_time: int

class RecommendationResponse(BaseModel):
    recipe_id: int
    title: str
    keycloak_user_id: str
    cooking_time: int
    rating_avg: float
    categories: List[str]
    ingredients: Optional[List[str]] = []

    model_config = {
        "from_attributes": True
    }
