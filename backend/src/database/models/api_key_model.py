from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.session import Base


class ApiKey(Base):
    __tablename__ = 'api_keys'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    api_key: Mapped[str] = mapped_column(String(128))
    private_key: Mapped[str] = mapped_column(String(128))