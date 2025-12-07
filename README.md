# STOXIFIED_BACKEND

Backend for the Stoxified application, providing news aggregation and user management APIs. Built with FastAPI and PostgreSQL.

## Features

- **News Aggregation**: Fetch and filter news articles from various sources.
- **User Management**: User signup, login, and authentication.
- **JWT Authentication**: Secure API access using JSON Web Tokens.
- **RESTful API**: Clean and documented API endpoints.

## Prerequisites

- Python 3.8+
- PostgreSQL

## Installation

1.  **Clone the repository**
    ```bash
    git clone <repository_url>
    cd STOXIFIED_BACKEND
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Linux/Mac
    source .venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration**
    Create a `.env` file in the root directory (you can copy `.env.example`) and add your database credentials:
    ```env
    DB_HOST=localhost
    DB_NAME=newsdb
    DB_USER=postgres
    DB_PASS=yourpassword
    DB_PORT=5432
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5.  **Database Setup**
    Ensure you have a PostgreSQL database named `newsdb` (or whatever you configured in `.env`) running.
    *Note: Ensure the `news` and `news_source` tables are created in your database.*

## Running the Application

Start the development server:

uvicorn app.main:app --reload

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

### News

-   **Get News**
    -   `GET /news`
    -   Parameters:
        -   `limit` (int, default=20): Number of articles to retrieve.
        -   `source` (str, optional): Filter by news source.
        -   `list_sources` (bool, default=false): If true, returns list of available sources.

-   **Get News Sources**
    -   `GET /news/sources`
    -   Returns a list of all distinct news sources.

### Users & Authentication

-   **Signup**
    -   `POST /signup`
    -   Body: `{"username": "str", "email": "str", "full_name": "str", "password": "str"}`

-   **Login**
    -   `POST /token`
    -   Body (Form Data): `username`, `password`
    -   Returns: Access token (JWT).

-   **Get Current User**
    -   `GET /users/me`
    -   Headers: `Authorization: Bearer <token>`
    -   Returns: Profile of the authenticated user.

## Project Structure

-   `app/main.py`: Application entry point.
-   `app/core/`: Configuration and database setup.
-   `app/routers/`: API route definitions.
-   `app/services/`: Business logic.
-   `app/schemas/`: Pydantic models.
-   `.env`: Environment variables.