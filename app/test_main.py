from fastapi.testclient import TestClient
from fastapi import status

def test_read_main(test_client: TestClient):
    response = test_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to version 0.0.test of FastAPI Test API"}