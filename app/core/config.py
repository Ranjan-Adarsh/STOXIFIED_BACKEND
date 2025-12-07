import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'newsdb')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASS', 'yourpassword')
    DB_PORT = os.getenv('DB_PORT', '5432')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dummy_secret_key')
    ALGORITHM = os.getenv('ALGORITHM', 'hs256')
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
