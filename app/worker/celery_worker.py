from time import sleep

from .celery_app import celery
from .tasks import RepeatTask



@celery.task(base=RepeatTask, acks_late=True, queue="test-queue", name="app.worker.celery_worker.test_celery")
def test_celery(*args, **kwargs) -> str:
    return {
        'args': args,
        'kwargs': kwargs,
    }
