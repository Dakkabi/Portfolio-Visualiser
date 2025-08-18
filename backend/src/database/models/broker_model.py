from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.session import Base
from backend.src.schemas.models.broker_enum import BrokerType


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True)
    type: Mapped[BrokerType] = mapped_column(ENUM(BrokerType, name="type_enum"), nullable=False)

    api_keys: Mapped[ApiKey] = relationship(back_populates="brokers")