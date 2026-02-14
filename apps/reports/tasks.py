import asyncio
import time

from celery import shared_task


@shared_task(bind=True)
def generate_heavy_sync_report(self, duration: int = 5) -> dict:
    time.sleep(duration)
    return {
        "status": "completed",
        "type": "sync",
        "duration": duration,
    }
