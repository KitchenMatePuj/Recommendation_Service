from src.main.python.config.databases_config import MongoDBClient

def save_recipe_document(document: dict):
    collection = MongoDBClient.get_collection()
    existing = collection.find_one({"recipe_id": document["recipe_id"]})

    if existing:
        collection.update_one(
            {"recipe_id": document["recipe_id"]},
            {"$set": document}
        )
        print(f"[~] Updated recipe in MongoDB: {document['recipe_id']}")
    else:
        collection.insert_one(document)
        print(f"[+] Inserted new recipe in MongoDB: {document['recipe_id']}")

def find_recipes_by_filters(categories: list, allergies: list, max_cooking_time: int):
    collection = MongoDBClient.get_collection()

    query = {
        "categories": {"$in": categories},
        "cooking_time": {"$lte": max_cooking_time},
        "ingredients": {
            "$not": {
                "$elemMatch": {"$in": allergies}
            }
        }
    }

    results = collection.find(query)
    return list(results)
