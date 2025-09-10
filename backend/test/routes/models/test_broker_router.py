from starlette.testclient import TestClient

from backend.src.main import app

client = TestClient(app)

def test_broker_get():
    response = client.get("/api/brokers")
    assert response.status_code == 200