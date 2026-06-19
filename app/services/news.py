
from typing import Optional
from sqlalchemy.orm import Session
from app.models.news import News, NewsSource

def get_news_list(db: Session, limit: int = 20, source: Optional[str] = None):
    query = db.query(News)
    if source:
        query = query.filter(News.source == source)
    return query.order_by(News.scraped_at.desc()).limit(limit).all()


def get_news_source_list(db: Session):
    results = db.query(NewsSource.source).distinct().order_by(NewsSource.source).all()
    return [row[0] for row in results]
