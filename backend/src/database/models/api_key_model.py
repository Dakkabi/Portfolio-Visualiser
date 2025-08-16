from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.session import Base


class ApiKey(Base):
    __tablename__ = 'api_keys'

    api_key: Mapped[str] = mapped_column(String, nullable=False)
    private_key: Mapped[str] = mapped_column(String)

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    users: Mapped["User"] = relationship(back_populates="api_keys")

    brokers_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), primary_key=True)
    brokers: Mapped["Broker"] = relationship(back_populates="api_keys")
