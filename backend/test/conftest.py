import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.src.core.config import settings
from backend.src.database.models.user_model import User
from backend.src.database.session import Base, get_db
from backend.src.main import app
from backend.src.services.security.auth_service import get_current_active_user

DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI
TEST_DATABASE_URI = DATABASE_URI.replace(settings.POSTGRESQL_DATABASE, settings.POSTGRESQL_TEST_DATABASE)

engine = create_engine(TEST_DATABASE_URI)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def override_get_db():
    def _override_get_db():
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        db = TestSessionLocal()
        yield db
        db.close()

    app.dependency_overrides[get_db] = _override_get_db
    yield

@pytest.fixture(scope="session", autouse=True)
def override_get_current_active_user():
    def _override_get_current_active_user():
        return User(
            id=1,
            email="email",
            password="password"
        )

    app.dependency_overrides[get_current_active_user] = _override_get_current_active_user