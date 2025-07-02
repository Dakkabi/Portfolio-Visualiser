import pytest

from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.main import app
from backend.src.services.auth.auth_service import get_current_active_user
from backend.test.database.test_session import db


@pytest.fixture(scope="session")
def dummy_active_user():
    return User(id=3, email="dummy@user.com", password="not_real")

@pytest.fixture(scope="function", autouse=True)
def override_dependencies(dummy_active_user, db):
    def _get_db_override():
        yield db

    app.dependency_overrides[get_db] = _get_db_override

    app.dependency_overrides[get_current_active_user] = lambda: dummy_active_user

    yield

    app.dependency_overrides.clear()