from src.main.python.config.databases_config import MongoDBClient

def save_recipe_document(document: dict):
    collection = MongoDBClient.get_collection()
    collection.update_one(
        {"recipe_id": document["recipe_id"]},
        {"$set": {"status": "processing"}},
        upsert=True
    )

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

    collection.update_one(
        {"recipe_id": document["recipe_id"]},
        {"$set": {"status": "ready"}}
    )


def update_recipe_document(document: dict):
    collection = MongoDBClient.get_collection()
    collection.update_one(
        {"recipe_id": document["recipe_id"]},
        {"$set": {"status": "processing"}}
    )
    result = collection.update_one(
        {"recipe_id": document["recipe_id"]},
        {"$set": document}
    )
    collection.update_one(
        {"recipe_id": document["recipe_id"]},
        {"$set": {"status": "ready"}}
    )
    print(f"[~] Updated recipe in MongoDB: {document['recipe_id']} | Matched: {result.matched_count}")


def delete_recipe_document(recipe_id: int):
    collection = MongoDBClient.get_collection()
    result = collection.delete_one({"recipe_id": recipe_id})
    print(f"[-] Deleted recipe: {recipe_id} | Deleted: {result.deleted_count}")


def add_ingredient_to_recipe(recipe_id: int, ingredient: dict):
    collection = MongoDBClient.get_collection()
    collection.update_one(
        {"recipe_id": recipe_id},
        {"$set": {"status": "processing"}}
    )
    result = collection.update_one(
        {"recipe_id": recipe_id},
        {"$addToSet": {"ingredients": ingredient["name"]}}
    )
    collection.update_one(
        {"recipe_id": recipe_id},
        {"$set": {"status": "ready"}}
    )
    print(f"[+] Added ingredient to recipe {recipe_id}: {ingredient['name']}")


def update_ingredient_in_recipe(recipe_id: int, ingredient: dict):
    collection = MongoDBClient.get_collection()
    collection.update_one(
        {"recipe_id": recipe_id},
        {"$set": {"status": "processing"}}
    )
    result = collection.update_one(
        {"recipe_id": recipe_id, "ingredients": ingredient["old_name"]},
        {"$set": {"ingredients.$": ingredient["name"]}}
    )
    collection.update_one(
        {"recipe_id": recipe_id},
        {"$set": {"status": "ready"}}
    )
    print(f"[~] Updated ingredient in recipe {recipe_id}: {ingredient['old_name']} -> {ingredient['name']}")


def delete_ingredient_from_recipe(recipe_id: int, ingredient_name: str):
    collection = MongoDBClient.get_collection()
    collection.update_one(
        {"recipe_id": recipe_id},
        {"$set": {"status": "processing"}}
    )
    result = collection.update_one(
        {"recipe_id": recipe_id},
        {"$pull": {"ingredients": ingredient_name}}
    )
    collection.update_one(
        {"recipe_id": recipe_id},
        {"$set": {"status": "ready"}}
    )
    print(f"[-] Removed ingredient from recipe {recipe_id}: {ingredient_name}")


def find_recipes_by_filters(categories: list, allergies: list, max_cooking_time: int):
    collection = MongoDBClient.get_collection()

    query = {
        "categories": {"$in": categories},
        "cooking_time": {"$lte": max_cooking_time},
        "ingredients": {
            "$not": {
                "$elemMatch": {"$in": allergies}
            }
        },
        "status": "ready",
        "rating_avg": {"$gte": 4.0, "$lte": 5.0}
    }

    results = collection.find(query)
    return list(results)
