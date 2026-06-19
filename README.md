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

6.  **Database Setup**
    Ensure you have a PostgreSQL database named `newsdb` (or whatever you configured in `.env`) running.
    *Note: Ensure the `news` and `news_source` tables are created in your database.*

## Deployment Notes

This repo is configured for GitHub-connected deployment via Docker.

### Recommended deployment flow

1. Connect the repository to a host such as Render, Railway, or Fly.
2. Use your Supabase PostgreSQL database as the app database.
3. Set these environment variables in the deployment provider:
   - `DB_HOST`
   - `DB_PORT`
   - `DB_NAME`
   - `DB_USER`
   - `DB_PASS`
   - `SECRET_KEY`
   - `ALGORITHM`
   - `ACCESS_TOKEN_EXPIRE_MINUTES`

### Docker

Build locally:

```bash
Docker build -t stoxified-backend .
```

Run locally:

```bash
docker run -e DB_HOST="$DB_HOST" -e DB_PORT="$DB_PORT" -e DB_NAME="$DB_NAME" -e DB_USER="$DB_USER" -e DB_PASS="$DB_PASS" -e SECRET_KEY="$SECRET_KEY" -p 8000:8000 stoxified-backend
```

### GitHub Actions

- `.github/workflows/ci.yml` checks secrets and validates app syntax.
- `.github/workflows/deploy.yml` builds a Docker image and pushes it to Docker Hub when `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` are configured.

### Docker Hub deployment

This repo can use Docker Hub as the deployment source so you do not need Render to clone the GitHub repo.

1. Create a Docker Hub repository, e.g. `yourusername/stoxified-backend`.
   - Docker Hub repo names must be lowercase and can only contain letters, numbers, `-`, `_`, or `.`.
   - Example valid names: `yourusername/stoxified-backend`, `yourusername/stoxified.backend`, `yourusername/stoxified_backend`.
   - Invalid: `yourusername/STOXIFIED_BACKEND`, `yourusername/Stoxified-Backend`.
2. In GitHub, add repository secrets:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
3. Push to `main`.
4. The workflow will build and push the image as `yourusername/stoxified-backend:latest`.
5. In Render (or another host), deploy from that Docker image instead of connecting to GitHub directly.

### Free-host keep-alive

If you are using a free plan, the service may sleep after a period of inactivity. To keep the app available longer:

1. Make sure your app exposes a health endpoint:
   - `HEAD /` returns status `200`
   - `GET /health` returns `{"status": "ok"}`
2. Configure an external uptime checker such as UptimeRobot, Cron-job.org, or a similar service.
3. Ping `https://<your-app-url>/health` every 5–10 minutes.

This keeps a free deployment awake more reliably, but it is still subject to the host's free-tier limits.
## Running the Application Locally

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