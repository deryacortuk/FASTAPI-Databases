from fastapi import FastAPI, Header, Depends,Request
from .routers.books import router_books


books = FastAPI()

books.include_router(router_books)

# def get_db():
#     with session() as db:
#         yield db

# @books.middleware("http")
# async def add_header(request:Request, call_next):
#     response = await call_next(request)
#     response.headers["X-Framework"] = "FastAPI"
#     return response
# async def verify_header(X-Web-Framework:str=Header()):
#     if X-Web-Framework != "FastAPI":
#         raise HTTPException(status_code=400,detail="Invalid Header")

# @books.get("/books", dependencies=[Depends(verify_header)])
# def get_books(db:Session=Depends(get_db)):
#     recs = db.query(Books).all()
#     return recs


