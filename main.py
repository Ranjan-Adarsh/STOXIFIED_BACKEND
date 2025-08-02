"""Main entry point for the FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router

app = FastAPI()

# CORS settings (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
