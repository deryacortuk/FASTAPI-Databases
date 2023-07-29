from fastapi import FastAPI, Depends, Body
from database.connection import get_db, Books

from typing import List 
import uvicorn
from models.book import BookModel
from sqlalchemy.orm import Session

app = FastAPI()


@app.post("/book", response_model=BookModel)
def add_book(book: BookModel, db: Session = Depends(get_db)):
    result = Books(**book.dict())  
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

@app.get("/books", response_model=List[BookModel])
def get_books(db:Session=Depends(get_db)):
    result = db.query(Books).all()
    return result
@app.get("/book/{id}",response_model=BookModel)
def get_book(id:int, db:Session=Depends(get_db)):
    return db.query(Books).filter(Books.id == id).first()

@app.put("/book/{id}", response_model=BookModel)
def update_book(id:int, price:int=Body(), db:Session=Depends(get_db)):
    book = db.query(Books).filter(Books.id == id).first()
    book.price = price 
    db.commit()
    return book
@app.delete("/book/{id}")
def delete_book(id:int, db:Session=Depends(get_db)):
    try:
        db.query(Books).filter(Books.id == id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return "Book was deleted successfully"
    
if __name__ == "__main__":
    uvicorn.run()
    
