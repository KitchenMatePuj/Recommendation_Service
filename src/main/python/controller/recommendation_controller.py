from typing import List

from fastapi import APIRouter
from src.main.python.services.recommendation_service import get_recommendations
from src.main.python.transformers.recommendation_transformer import RecommendationResponse, RecommendationRequest

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.post("/", response_model=List[RecommendationResponse])
def list_recommendations(request: RecommendationRequest):
    return get_recommendations(
        favorite_categories=request.favorite_categories,
        allergies=request.allergies,
        cooking_time=request.cooking_time
    )

