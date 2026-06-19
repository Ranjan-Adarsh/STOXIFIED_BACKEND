from fastapi import HTTPException
import psycopg2
from app.core.database import connect_db
from app.core.security import get_password_hash
from app.schemas.user import UserCreate

def create_user(username, email, full_name, password):
    """User management functions for FastAPI application"""
    hashed_password = get_password_hash(password)
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT 1 FROM users WHERE username = %s OR email = %s",
            (username, email),
        )
        if cur.fetchone():
            raise HTTPException(status_code=400, detail="Username or email already exists")

        cur.execute("""
            INSERT INTO users (username, email, full_name, hashed_password)
            VALUES (%s, %s, %s, %s) RETURNING id;
        """, (username, email, full_name, hashed_password))
        user_id = cur.fetchone()[0]
        conn.commit()
        return {"id": user_id, "username": username, "email": email, "full_name": full_name, "is_active": True}
    except HTTPException:
        conn.rollback()
        raise
    except psycopg2.errors.UniqueViolation as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Username or email already exists") from e
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Unable to create user") from e
    finally:
        cur.close()
        conn.close()


def get_user_by_username(username):
    """Retrieve user by username"""
    if not username:
        raise HTTPException(status_code=400, detail="Username must be provided")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, username, email, full_name, hashed_password, is_active FROM users WHERE username = %s", (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "email": row[2], "full_name": row[3], "hashed_password": row[4], "is_active": row[5]}
    return None
