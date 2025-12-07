from typing import Optional, List
from app.core.database import connect_db

def get_news_list(limit: int = 20, source: Optional[str] = None):
    conn = connect_db()
    cursor = conn.cursor()

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
            "scraped_at": row[5]
        }
        for row in rows
    ]
    return news_list

def get_news_source_list():
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
