import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm.session import Session, sessionmaker

from backend.src.core.config import settings
from backend.src.database.session import get_db, Base


@pytest.fixture
def db() -> Session:
    DATABASE_TEST_URI = settings.SQLALCHEMY_TEST_DATABASE_URI
    engine = create_engine(str(DATABASE_TEST_URI))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE"))
        conn.execute(text("CREATE SCHEMA public"))
        Base.metadata.create_all(bind=conn)

    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

def test_db(prod_db = next(get_db())):
    assert prod_db is not None