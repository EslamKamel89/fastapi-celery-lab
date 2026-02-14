from celery import Celery

# i have to import the apps here because if i don't i will get apps module not found error
import apps
from core.config import settings


def create_celery_app() -> Celery:
    app = Celery("fastapi_worker")
    app.conf.update(
        broker_url=f"{settings.REDIS_URL}/0",
        result_backend=f"{settings.REDIS_URL}/1",
        task_track_started=True,
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
        timezone="UTC",
        enable_utc=True,
        task_acks_late=True,
        worker_prefetch_multiplier=1,
    )

    app.autodiscover_tasks(["apps"])
    return app


celery_app = create_celery_app()
