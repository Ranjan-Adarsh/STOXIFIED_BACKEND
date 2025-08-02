from fastapi import APIRouter
from database import connect_db
from typing import Optional

router = APIRouter()

@router.get("/news")
def get_news(limit: int = 20, source: Optional[str] = None, list_sources: bool = False):
    conn = connect_db()
    cursor = conn.cursor()

    if list_sources:
        cursor.execute('''
            SELECT DISTINCT source
            FROM news_source
            ORDER BY source
        ''')
        sources = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return {"sources": sources}

    if source:
        cursor.execute('''
            SELECT id, headline, url, summary, source, scraped_at
            FROM news
            WHERE source = %s
            ORDER BY scraped_at DESC
            LIMIT %s
        ''', (source, limit))
    else:
        cursor.execute('''
            SELECT id, headline, url, summary, source, scraped_at
            FROM news
            ORDER BY scraped_at DESC
            LIMIT %s
        ''', (limit,))

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    news_list = [
        {
            "id": row[0],
            "headline": row[1],
            "url": row[2],
            "summary": row[3],
            "source": row[4],
            "scraped_at": row[5].isoformat() if row[5] else None
        }
        for row in rows
    ]
    return {"news": news_list}

@router.get("/news/sources")
def get_news_sources():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT DISTINCT source
        FROM news_source
        ORDER BY source
    ''')
    sources = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return sources
