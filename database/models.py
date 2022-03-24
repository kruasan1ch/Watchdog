from sqlalchemy import Column, Integer, String, Date, DateTime

from database.database import Base


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    link = Column(String(64), unique=True, index=True)
    type = Column(Integer, nullable=True)
    last_chapter = Column(String(64), nullable=True)
    last_check = Column(Date, nullable=True)
    last_update = Column(DateTime, nullable=True)
