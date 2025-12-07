from fastapi import APIRouter, Depends
from typing import Optional, List, Union
from app.schemas.news import NewsList, NewsSourceList
from app.services.news import get_news_list, get_news_source_list

router = APIRouter(prefix="/news", tags=["News"])

@router.get("", response_model=Union[NewsList, NewsSourceList])
def get_news(limit: int = 20, source: Optional[str] = None, list_sources: bool = False):
    if list_sources:
        sources = get_news_source_list()
        return {"sources": sources}
    
    news = get_news_list(limit, source)
    return {"news": news}

@router.get("/sources", response_model=List[str])
def get_news_sources():
    return get_news_source_list()
