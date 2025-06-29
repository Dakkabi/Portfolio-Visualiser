from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from backend.src.database.models.api_key_model import ApiKey
from backend.src.database.session import Base

class Broker(Base):
    __tablename__ = 'broker'

    name: Mapped[String] = MappedColumn(String(64), unique=True, primary_key=True)

    api_keys: Mapped[list["ApiKey"]] = relationship("ApiKey", back_populates="broker")