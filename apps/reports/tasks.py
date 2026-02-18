import asyncio
import time
from typing import Sequence

from celery import shared_task
from sqlalchemy import select

from apps.auth.models import User
from core.worker_database import SessionLocal


async def _fetch_all_users():
    async with SessionLocal() as session:
        res = await session.execute(select(User))
        return [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
            for user in res.scalars().all()
        ]


@shared_task(bind=True)
def generate_heavy_sync_report(self, duration: int = 5) -> dict:
    time.sleep(duration)
    users = asyncio.run(_fetch_all_users())
    return {
        "status": "completed",
        "type": "sync",
        "duration": duration,
        "users": users,
    }
