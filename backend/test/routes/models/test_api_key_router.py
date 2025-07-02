import pytest
from fastapi.testclient import TestClient

from backend.src.database.session import get_db
from backend.src.main import app

client = TestClient(app)
url_prefix = "/api/api-keys"

@pytest.fixture(autouse=True)
def override_dependency_db(db):
    def _get_db_override():
        yield db
    app.dependency_overrides[get_db] = _get_db_override

def create_and_delete_api_keys():
    pass