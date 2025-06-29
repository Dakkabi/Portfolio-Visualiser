from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.session import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    password: Mapped[str] = mapped_column(String(128))

    api_keys: Mapped[list["ApiKey"]] = relationship("ApiKey", back_populates="user")
