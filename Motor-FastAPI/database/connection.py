from motor import motor_asyncio

def get_collection():
    client = motor_asyncio.AsyncIOMotorClient()
    DB = "pydata"
    collection = "books"
    db = client[DB][collection]
    yield db