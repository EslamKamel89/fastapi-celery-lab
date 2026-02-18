from typing import Annotated

from celery.result import AsyncResult
from fastapi import APIRouter, Query

from apps.reports.tasks import generate_heavy_sync_report

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/heavy-report")
async def create_heavy_report(duration: Annotated[int, Query(gt=0)] = 5):
    task: AsyncResult = generate_heavy_sync_report.delay(duration)  # type: ignore
    return {
        "task_id": task.id,
        "status": "submitted",
    }
