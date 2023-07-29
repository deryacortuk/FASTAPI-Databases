from pydantic import BaseModel

class BookModel(BaseModel):
    id:int
    title:str
    author:str
    price:int
    publisher:str