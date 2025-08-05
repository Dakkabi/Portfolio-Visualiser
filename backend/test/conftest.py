import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.src.core.config import settings
from backend.src.database.crud.user_crud import create_db_user
from backend.src.database.models.user_model import User
from backend.src.database.session import Base, get_db
from backend.src.main import app
from backend.src.schemas.model.user_schema import UserCreate
from backend.src.services.security.auth_service import get_current_active_user

DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI
TEST_DATABASE_URI = DATABASE_URI.replace(settings.POSTGRESQL_DATABASE, settings.POSTGRESQL_TEST_DATABASE)
engine = create_engine(TEST_DATABASE_URI)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

test_cache = {}

@pytest.fixture
def db_user(get_test_db):
    if "user" in test_cache:
        return test_cache["user"]

    new_user = UserCreate(
        email="test@test.com",
        password="test",
    )
    db_user = create_db_user(get_test_db, new_user)
    test_cache["user"] = db_user
    return db_user

@pytest.fixture(scope="session", autouse=True)
def get_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="session", autouse=True)
def override_get_db(get_test_db):
    def _get_db():
        return get_test_db

    app.dependency_overrides[get_db] = _get_db

@pytest.fixture(scope="session", autouse=True)
def override_get_current_active_user():
    def _override_get_current_active_user():
        return User(
            id=1,
            email="email",
            password="password"
        )

    app.dependency_overrides[get_current_active_user] = _override_get_current_active_user