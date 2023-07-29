from fastapi import FastAPI, Depends, Body
from database.connection import get_collection
import uvicorn
from typing import List
from models.book import BookModel

app = FastAPI()

@app.post("/book")
def add_book(book:BookModel,db=Depends(get_collection)):
    result = db.insert_one(book.dict())
    return "Book was added successfully"

@app.get("/books",response_model=List[BookModel])
def get_books(db=Depends(get_collection)):
    books = list(db.find())
    return books 

@app.get("/book/{id}",response_model=BookModel)
def get_book(id:str,db=Depends(get_collection)):
    book = db.find_one({"_id":id})    
    return book

@app.put("/book/{id}")
def update_book(id:str,book:BookModel, db=Depends(get_collection)):
    db.find_one_and_update({"_id":id},{"$set":dict(book)})
    return "Book was updated"

@app.delete("/book/{id}")
def delete_book(id:str,db=Depends(get_collection)):
    db.find_one_and_delete({"bookID":id})
    return "Book was deleted successfully"




if __name__ == "__main__":
    uvicorn.run()
    