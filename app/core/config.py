import os
import warnings
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'newsdb')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASS')
    DB_PORT = int(os.getenv('DB_PORT', '5432'))
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '30'))


settings = Settings()

# Security checks: require SECRET_KEY and warn on missing DB_PASS
if not settings.SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY environment variable is not set. Set it in your environment or .env (do not commit secrets)."
    )

if settings.DB_PASS is None:
    warnings.warn(
        "DB_PASS is not set. Using an empty DB password may be insecure.", UserWarning
    )
