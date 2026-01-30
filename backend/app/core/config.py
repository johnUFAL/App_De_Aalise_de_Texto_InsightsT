#cofigurações sobre a aplicação
from pydantic_settings import BaseSettings # type: ignore
import os

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "https://seusite.onrender.com")
    
    class Config:
        env_file = ".env"