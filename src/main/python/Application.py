from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.main.python.controller.recommendation_controller import router as recommendation_router
from src.main.python.rabbit.rabbit_listener import start_rabbit_listener
import threading

def create_app() -> FastAPI:
    app = FastAPI(
        title="Recommendation Service",
        description="Recommends recipes based on preferences, allergies and time availability",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:4200", 'http://localhost:8080'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(recommendation_router)

    threading.Thread(target=start_rabbit_listener, daemon=True).start()

    return app

app = create_app()
