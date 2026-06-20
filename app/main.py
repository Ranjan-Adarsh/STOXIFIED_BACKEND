from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, users, news

app = FastAPI(title="Stoxified Backend")

# CORS settings (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://stoxified.vercel.app",
        "https://stoxified-git-main-stoxified.vercel.app",
    ],
    allow_origin_regex=r"https://stoxified-.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(news.router)

@app.head("/")
def root_head():
    return Response(status_code=200)

@app.get("/")
def root():
    return {"message": "Welcome to Stoxified Backend API"}

@app.get("/health")
def health():
    return {"status": "ok"}
