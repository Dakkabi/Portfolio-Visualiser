from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.session import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    password: Mapped[str] = mapped_column(String(255))

    api_keys: Mapped[list["ApiKey"]] = relationship("ApiKey", back_populates="user")
