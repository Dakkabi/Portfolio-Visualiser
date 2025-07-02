from fastapi.testclient import TestClient

from backend.test.conftest import *

client = TestClient(app)
url_prefix = "/api/api-keys"

def create_and_delete_api_keys():
    pass