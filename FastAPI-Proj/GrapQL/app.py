from fastapi import FastAPI
import uvicorn

app = FastAPI()

import strawberry

@strawberry.type
class Book:
    title:str
    author:str
    price:int

@strawberry.type
class Query:
    @strawberry.field
    def book(self)->Book:
        return Book(title="Test",author="new1",price=27)
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title:str, author:str, price:int)->Book:
        return Book(title=title,author=author, price=price)
        
    
from strawberry.asgi import GraphQL

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app.add_route("/book",graphql_app)

if __name__ == "__main__":
    uvicorn.run()


# type Book {
#     title:String!, ! means required 
#     price:Int!
# }

# books is root query, title field is payload of the query

#  Grapql uses MUTATİONS (3 types mutations -- create or add ne data, update or modify data, delete data)
# mutation {
#     createBook(title: "python") {
#         title 
#         price
#     }
# }
# subscription{
#     newBook{
#         title 
#         price
#     }
# }

# GraphQL schema is a collection of Grapql root types.
# type Query {}
# type Mutation {}
# type Subscription{} 

# Library for Grapql 
# Adriadne, Strawberry, Tartiflette, Graphene

# pip install strawberry-graphql[fastapi]

