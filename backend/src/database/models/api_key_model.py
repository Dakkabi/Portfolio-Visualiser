from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.models.user_model import User
from backend.src.database.session import Base


class ApiKey(Base):
    __tablename__ = 'api_keys'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    api_key: Mapped[str] = mapped_column(Text)
    private_key: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship("User", back_populates="api_keys")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    broker: Mapped["Broker"] = relationship("Broker", back_populates="api_keys")
    broker_name: Mapped[str] = mapped_column(String(128), ForeignKey("brokers.name"))