from fastapi.testclient import TestClient

from fastapi import status
from .app import app

# app.depencenct_overrides[get_db] = test_get_db

client = TestClient(app)  # not support async if wanted use HTTPX AsyncClient 

def test_list():
    response = client.get("/list/2")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"title":"Pyhton 3","price":133}
    
def test_add_new():
    response = client.post("/list", json={"title":"Pyhton 23","price":1533})
    assert response.status_code == status.HTTP_201_CREATED