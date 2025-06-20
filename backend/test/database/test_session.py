from sqlalchemy import create_engine
from backend.src.core.config import settings
from backend.src.database.session import get_db, Base
import pytest
from sqlalchemy.orm.session import Session, sessionmaker


@pytest.fixture
def db() -> Session:
    DATABASE_TEST_URI = settings.SQLALCHEMY_TEST_DATABASE_URI
    engine = create_engine(str(DATABASE_TEST_URI))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = SessionLocal()

    base = Base()
    base.metadata.drop_all(bind=engine)
    base.metadata.create_all(bind=engine)

    yield db_session

    db_session.close()

def test_db(prod_db = next(get_db())):
    assert prod_db is not None