from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass
class Event (Base):
    __tablename__ = "Event"
    id: Mapped[int] =mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    comment: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return  f"Event(id={self.id}), name ={self.name}, comment = {self.comment})"
