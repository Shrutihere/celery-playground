from time import sleep

from celery import current_task

from .celery_app import celery


@celery.task(acks_late=True, queue="test-queue", name="app.worker.celery_worker.test_celery")
def test_celery(word = "default word") -> str:
    return f"test task return {word}"
