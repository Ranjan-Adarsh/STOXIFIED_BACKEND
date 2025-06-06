from fastapi import APIRouter
from database import connect_db

router = APIRouter()

@router.get("/news")
def get_news(limit: int = 20):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, headline, url, summary, source, scraped_at
        FROM news
        ORDER BY scraped_at DESC
        LIMIT %s
    ''', (limit,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    news_list = []
    for row in rows:
        news_list.append({
            "id": row[0],
            "headline": row[1],
            "url": row[2],
            "summary": row[3],
            "source": row[4],
            "scraped_at": row[5].isoformat() if row[5] else None
        })
    return news_list
