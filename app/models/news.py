# app/models/news.py
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    headline = Column(String)
    url = Column(String)
    summary = Column(String)
    source = Column(String)
    scraped_at = Column(DateTime)

class NewsSource(Base):
    __tablename__ = "news_source"   
    id = Column(Integer, primary_key=True)
    source = Column(String, unique=True)