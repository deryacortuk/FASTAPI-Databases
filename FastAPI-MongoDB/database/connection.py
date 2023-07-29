from pymongo import MongoClient

def get_collection():
    client = MongoClient()
    DB = "pydata"
    collection = "books"
    bjson = client[DB][collection]
    yield bjson