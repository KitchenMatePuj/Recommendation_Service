from fastapi import FastAPI
from src.main.python.controller.recommendation_controller import router as recommendation_router
from src.main.python.rabbit.rabbit_listener import start_rabbit_listener
import threading

def create_app() -> FastAPI:
    app = FastAPI(
        title="Recommendation Service",
        description="Recommends recipes based on preferences, allergies and time availability",
        version="1.0.0"
    )

    app.include_router(recommendation_router)

    # Start RabbitMQ listener in background thread
    threading.Thread(target=start_rabbit_listener, daemon=True).start()

    return app

app = create_app()