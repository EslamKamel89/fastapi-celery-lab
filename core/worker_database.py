from dotenv import load_dotenv

load_dotenv()

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import settings

if not settings.DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in the env variables")
engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
    future=True,
)
SessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, autoflush=False, class_=AsyncSession
)
