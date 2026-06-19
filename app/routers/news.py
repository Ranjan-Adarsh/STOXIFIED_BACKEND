from fastapi import APIRouter, Depends
from typing import Optional, List
from sqlalchemy.orm import Session
from app.schemas.news import NewsList
from app.services.news import get_news_list, get_news_source_list
from app.core.database import get_db

router = APIRouter(prefix="/news", tags=["News"])

@router.get("", response_model=NewsList)
def get_news(
    limit: int = 20,
    source: Optional[str] = None,
    db: Session = Depends(get_db),
):
    news = get_news_list(db, limit, source)
    return {"news": news}

@router.get("/sources", response_model=List[str])
def get_news_sources(db: Session = Depends(get_db)):
    return get_news_source_list(db)