import os

from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI app")
    DATABASE_URL: str | None = os.getenv("DATABASE_URL", None)
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")


settings = Settings()
