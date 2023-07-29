from fastapi import FastAPI
from pydantic import BaseModel

import hypercorn

app = FastAPI()

class BookModel(BaseModel):
    title:str
    price:int
    
books = [
    {"title":"Pyhton 1","price":13}, {"title":"Pyhton 3","price":133}, 
    {"title":"Pyhton 4","price":132}, {"title":"Pyhton 5","price":143}
]

@app.get("/list/{id}")
async def get_list(id:int):
    return books[id-1]

@app.post("/list",status_code=201)
async def add_new(book:BookModel):
    books.append(book.dict())
    return book

if __name__ == "__main__":
    hypercorn.run()