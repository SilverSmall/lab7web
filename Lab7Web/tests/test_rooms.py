from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_room():
    response = client.post("/rooms/", json={"number": "101A", "capacity": 3})
    assert response.status_code == 200
    assert response.json()["number"] == "101A"

def test_read_rooms():
    response = client.get("/rooms/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
