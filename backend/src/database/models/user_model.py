from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    api_keys: Mapped[ApiKey] = relationship(back_populates="users")