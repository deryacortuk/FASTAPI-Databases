from fastapi import FastAPI, Depends, Body
import uvicorn
from database.db import get_cursor, init_db
from models.books import BookModel


app = FastAPI()

@app.on_event("startup")
def on_startup():    
    init_db()

@app.post("/")
def add_book(book:BookModel, db=Depends(get_cursor)):
    id = book.id
    title = book.title
    author = book.author
    price = book.price
    publisher = book.publisher    
    conn = db[0]
    cur = db[1]
    qry = "INSERT INTO Books VALUES(?,?,?,?,?)"
    cur.execute(qry,(id,title,author,price,publisher))
    conn.commit()
    return "Book successfully added."    

@app.get("/books")
def get_books(db=Depends(get_cursor)):
    conn = db[0]
    cur = db[1]
    
    cur.execute("select * from Books")
    books = cur.fetchall()
    conn.close()
    return books

@app.get("/book/{id}")
def get_book(id:int,db=Depends(get_cursor)):
    conn = db[0]
    cur = db[1]
    qry = "select * from Books where id=?"
    book = cur.execute(qry,(id,))
    rst = book.fetchone()
    conn.close()
    return rst

@app.put("/book/{id}")
def update_book(id:int,price:int=Body(),db=Depends(get_cursor)):
    conn = db[0]
    cur = db[1]
    qry = "update Books set price=? where id=?"
    cur.execute(qry,(price,id))
    conn.commit()
    return {"Book was updated successfully"}
@app.delete("/book/{id}")
def delete_book(id:int, db=Depends(get_cursor)):
    conn = db[0]
    cur = db[1]
    qry = "delete from Books where id=?"
    cur.execute(qry,(id,))
    conn.commit()
    return "Book was deleted successfully"
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",port=8000, reload=True)
    