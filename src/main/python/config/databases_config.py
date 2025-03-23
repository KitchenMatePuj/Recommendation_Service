from pymongo import MongoClient
from src.main.python.ApplicationProperties import ApplicationProperties

class MongoDBClient:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = MongoClient(ApplicationProperties.MONGO_URI)
        return cls._client

    @classmethod
    def get_database(cls):
        return cls.get_client()[ApplicationProperties.MONGO_DB]

    @classmethod
    def get_collection(cls):
        return cls.get_database()[ApplicationProperties.MONGO_COLLECTION]
