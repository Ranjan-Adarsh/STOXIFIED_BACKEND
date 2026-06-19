from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class NewsItem(BaseModel):
    id: int
    headline: str
    url: str
    summary: Optional[str] = None
    source: str
    scraped_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class NewsList(BaseModel):
    news: list[NewsItem]

class NewsSourceList(BaseModel):
    sources: list[str]
