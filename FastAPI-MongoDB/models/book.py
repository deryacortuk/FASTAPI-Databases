from pydantic import BaseModel

class BookModel(BaseModel):
    
    title:str
    author:str
    price:int
    publisher:str