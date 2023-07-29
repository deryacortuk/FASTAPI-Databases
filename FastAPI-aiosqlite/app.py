from fastapi import FastAPI, Depends, Body
import uvicorn
from database.connection import init_db, get_cursor
from models.bookmodel import BookModel


app = FastAPI()

@app.on_event("startup")
async def on_startup():    
    await init_db()

@app.post("/book")
async def book_post(book:BookModel, db=Depends(get_cursor)):
    id = book.id
    author = book.author
    title = book.title
    price = book.price
    publisher = book.publisher
    
    conn = db[0]
    cursor = db[1]
    
    query = "insert into Books values(?,?,?,?,?)"
    await cursor.execute(query,(id,author,title,price,publisher))
    await conn.commit()
    return "Success"

@app.get("/books")
async def get_books(db=Depends(get_cursor)):
    conn = db[0]
    cursor = db[1]
    books = await cursor.execute("Select * from Books")
    results = await books.fetchall()
    await conn.close()
    return results

@app.get("/book/{id}")
async def get_book(id:int, db=Depends(get_cursor)):
    conn = db[0]
    cur = db[1]
    qry = "Select * from Books where id=?"
    result = await cur.execute(qry,(id,))
    book = await result.fetchone()
    await conn.close()
    return book
@app.put("/book/{id}")
async def update_book(id:int, price:int=Body(),title:str=Body(), db=Depends(get_cursor)):
    conn = db[0]
    cursor = db[1]
    qry = "UPDATE books SET price=?, title=? WHERE id=?"  
    await cursor.execute(qry, (price, title, id))
    await conn.commit()
    return {"message": "Success"}
@app.delete("/book/{id}")
async def delete_book(id:int, db=Depends(get_cursor)):
    conn = db[0]
    cur = db[1]
    qry = "delete from books where id=?"
    await cur.execute(qry,(id,))
    await conn.commit()
    return {"Deleted book"}
    
    
    
    
    
    

if __name__ == "__main__":
    uvicorn.run()