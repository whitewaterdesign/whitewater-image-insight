from fastapi.testclient import TestClient
from fastapi import status

def test_read_health(test_client: TestClient):
    response = test_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}