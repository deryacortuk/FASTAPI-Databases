from pydantic import BaseModel

class BookModel(BaseModel):
    title:str
    author:str
    publisher:str
    price:int