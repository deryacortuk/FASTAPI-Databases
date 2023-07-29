from fastapi import FastAPI, Depends, Body
import uvicorn
from models.book import BookModel
from database.connection import booklist, get_db
from typing import List
app = FastAPI()

@app.post("/book",response_model=BookModel)
async def book_post(book:BookModel,db=Depends(get_db)):
    query = booklist.insert().values(id=book.id,title=book.title,author=book.author,price=book.price)
    await db.execute(query)
    return "Book was added successfully"

@app.get("/books",response_model=List[BookModel])
async def get_books(db=Depends(get_db)):
    query = booklist.select()
    return await db.fetch_all(query)

@app.get("/book/{id}",response_model=BookModel)
async def get_book(id:int, db=Depends(get_db)):
    query = booklist.select().where(booklist.c.id==id)
    return await db.fetch_one(query)

@app.put("/book/{id}")
async def update_book(id:int, title:str=Body(),db=Depends(get_db)):
    query = booklist.update().where(booklist.c.id==id).values(title=title)
    await db.execute(query)
    return "Book was updated successfully"

@app.delete("/book/{id}")
async def book_delete(id:int, db=Depends(get_db)):
    query = booklist.delete().where(booklist.c.id==id)
    await db.execute(query)
    return "Book was deleted."
    
    




if __name__ == "__main__":
    uvicorn.run()