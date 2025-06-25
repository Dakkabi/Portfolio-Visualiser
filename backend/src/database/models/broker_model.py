from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, MappedColumn

from backend.src.database.session import Base

class Broker(Base):
    __tablename__ = 'broker'

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)
    name: Mapped[String] = MappedColumn(String(64), unique=True)