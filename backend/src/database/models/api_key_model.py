from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.session import Base


class ApiKey(Base):
    __tablename__ = 'api_keys'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    api_key: Mapped[str] = mapped_column(String(128))
    private_key: Mapped[str] = mapped_column(String(128))

    user: Mapped["User"] = relationship("User", back_populates="api_keys")
    broker: Mapped["Broker"] = relationship("Broker", back_populates="api_keys")