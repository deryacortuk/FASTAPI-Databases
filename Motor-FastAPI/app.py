from fastapi import FastAPI, Depends
import uvicorn
from database.connection import get_collection
from models.book import BookModel
from typing import List 


app = FastAPI()

@app.post("/books")
async def add_book(book:BookModel,db=Depends(get_collection)):
    await db.insert_one(book.dict())
    return "Book was added successfully"

@app.get("/books",response_model=List[BookModel])
async def get_books(db=Depends(get_collection)):
    books = await db.find().to_list(1000)
    return books 
@app.get("books/{id}",response_model=BookModel)
async def get_book(id:str,db=Depends(get_collection)):
    book = await db.find_one({"_id":id})
    return book

@app.put("/books/{id}")
async def update_book(id:str,book:BookModel ,db=Depends(get_collection)):
    await db.find_one_and_update({"_id":id},{"$set":dict(book)})
    return "Book was updated successfully"

@app.delete("/books/{id}")
async def delete_book(id:str,db=Depends(get_collection)):
    await db.find_one_and_delete({"_id":id})
    return "Book was deleted successfully"



if __name__ == "__main__":
    uvicorn.run()
