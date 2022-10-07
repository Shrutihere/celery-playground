import logging
from app.models.rrule import Task
from app.worker.schedule import TaskScheduler
from fastapi import BackgroundTasks, APIRouter
from app.worker.celery_worker import test_celery


router = APIRouter(prefix="/tasks")

log = logging.getLogger(__name__)


def celery_on_message(body):
    log.warn(body)

def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propagate=False))



@router.post("/remind_me")
async def root(input: Task, background_task: BackgroundTasks):
    print(input)
    
    task_id = TaskScheduler.schedule(
            func=test_celery,
            description='Test task',
            trigger_at=input.start_datetime,
            args=["there it is"],
            kwargs={
                # "auth":input.auth,
                # "inserted_id": input.inserted_id,
                # "classroom_id": input.classroom_id
                "notification_metadata": input.notification_metadata
            },
            rrule_string=input.rrule,
        )
    print(task_id)
    background_task.add_task(background_on_message, task_id)

    return {"message": "success"}