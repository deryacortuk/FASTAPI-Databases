from fastapi import FastAPI, Request, Depends,Header, HTTPException
from fastapi.responses import Response
from albums.albums import albums
from books.books import books

from flask_main import flask_app
from fastapi.middleware.wsgi import WSGIMiddleware

from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer

# scheme = HTTPBasic()

sheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/")
# def index(loginfo:HTTPBasicCredentials=Depends(scheme)):
#     return {"message":"Hello {}".loginfo.username}

import uvicorn

app = FastAPI()

def credentials(request):
    dct = request.cookies
    try:
        return dct["api_key"]
    except:
        return None
persons = [{"name":"Derya"}]
    
@app.get("/user/")
async def get_user(key=Depends(credentials(Request))):
    if key == None:
        return {"message":"API key not validated"}
    else:
        return persons


@app.get("/")
async def index(request:Request,response:Response):
    response.set_cookie(key="user",value="admin")
    response.set_cookie(key="api_key",value="a12334ddd")
    return {"message":"Home page"}

app.mount("/albumapi",albums)
app.mount("/bookapi",books)
app.mount("/flask", WSGIMiddleware(flask_app))

if __name__ == "__main__":
    uvicorn.run()
    