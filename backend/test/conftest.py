import pytest

from backend.src.database.crud.user_crud import create_db_user
from backend.src.database.models.user_model import User
from backend.src.database.session import get_db
from backend.src.main import app
from backend.src.schemas.model.user_schema import UserCreate
from backend.src.services.auth.auth_service import get_current_active_user
from backend.test.database.test_session import db


@pytest.fixture
def global_secret_key():
    return "96U4uCt0mB4X2gRFvdAUNVI0S8OsLVnzjxuy6tFaWv0="

@pytest.fixture
def dummy_active_user(db):
    return create_db_user(
        db,
        UserCreate(
            email="dummy@user.com",
            password="password"
        )
    )

@pytest.fixture(scope="function", autouse=True)
def override_dependencies(dummy_active_user, db):
    def _get_db_override():
        yield db

    app.dependency_overrides[get_db] = _get_db_override

    app.dependency_overrides[get_current_active_user] = lambda: dummy_active_user

    yield

    app.dependency_overrides.clear()