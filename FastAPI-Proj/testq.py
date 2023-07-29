import pytest  
from httpx import AsyncClient 
from .app import app 

@pytest.mark.anyio
async def test_list():
    async with AsyncClient(app=app, base_url="") as ac:
        response = await ac.get("/list/1")
        assert response.status_code == 200
        assert response.json() == {"title":"Pyhton 5","price":143}
