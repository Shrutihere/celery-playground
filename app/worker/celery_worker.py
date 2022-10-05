from time import sleep

from .celery_app import celery
from .tasks import RepeatTask
from app.adapters.notifications.methods.edvora_notification import EdvoraNotification
from app.adapters.notifications.methods.notification_types import (
    title_from_type,
    create_title,
)
from app.adapters.notifications.constants import (
    EVENT_CREATED,
    TIMELINE_SESSION
)





@celery.task(base=RepeatTask, acks_late=True, queue="test-queue", name="app.worker.celery_worker.test_celery")
def test_celery(*args, **kwargs) -> str:

    EdvoraNotification(
            auth_header=kwargs["auth"],
            title=create_title(
                type=EVENT_CREATED,
                first_variable="hello",
                second_variable="kolkata",
            ),
            body="welcomeeee",
            item_id=kwargs["inserted_id"],
            created_at=1663593360,
            created_by="sh",
            classroom_id=kwargs["classroom_id"],
            kind=TIMELINE_SESSION,
        ).send()


    return {
        'args': args,
        'kwargs': kwargs,
    }
