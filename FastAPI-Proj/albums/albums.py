from fastapi import FastAPI
from .routers.albums import router_albums


albums = FastAPI()

albums.include_router(router_albums)


