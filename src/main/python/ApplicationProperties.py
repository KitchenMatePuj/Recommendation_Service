import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationProperties:
    RABBIT_HOST = os.getenv("RABBIT_HOST", "localhost")
    RABBIT_PORT = int(os.getenv("RABBIT_PORT", 5672))
    RABBIT_USER = os.getenv("RABBIT_USER", "guest")
    RABBIT_PASSWORD = os.getenv("RABBIT_PASSWORD", "guest")
    RABBIT_QUEUE = os.getenv("RABBIT_QUEUE", "recipes")

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB = os.getenv("MONGO_DB", "recommendations_db")
    MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "recipes")
