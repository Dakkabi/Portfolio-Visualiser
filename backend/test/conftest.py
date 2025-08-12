from typing import Generator

import pytest
from sqlalchemy import create_engine, True_
from sqlalchemy.orm import sessionmaker

from backend.src.core.config import settings
from backend.src.core.services.auth.auth_service import get_current_active_user
from backend.src.database.models.user_model import User
from backend.src.database.session import Base, get_db
from backend.src.main import app

# Test Database Setup
SQLALCHEMY_TEST_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI.replace(
    settings.POSTGRESQL_DATABASE,
    settings.POSTGRESQL_TEST_DATABASE
)
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URI)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db() -> Generator:
    db = TestSessionLocal()

    try:
        yield db
    finally:
        db.close()

def override_get_current_active_user() -> User:
    return User(
        id=1,
        email="test@test.com",
        password="password"
    )


@pytest.fixture(scope="session", autouse=True)
def override_dependency():
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_active_user] = override_get_current_active_user

    yield

    app.dependency_overrides = {}
