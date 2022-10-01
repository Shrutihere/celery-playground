import os
import uvicorn
import logging
from fastapi import FastAPI, BackgroundTasks
from worker.celery_app import celery
from worker.celery_worker import test_celery
from datetime import datetime, timedelta
from dateutil.rrule import rrulestr
from worker.schedule import TaskScheduler



log = logging.getLogger(__name__)

app = FastAPI()


def celery_on_message(body):
    log.warn(body)

def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propagate=False))



# queue tasks using task_names
@app.get("/{word}")
async def root(word: str, background_task: BackgroundTasks):

    # set correct task name based on the way you run the example
    task_name = "app.worker.celery_worker.test_celery"

    task = celery.send_task(task_name, args=[word], queue="test-queue")
    print(task)
    background_task.add_task(background_on_message, task)

    return {"message": "Word received"}




# Funtion takes time in seconds and execute task after x seconds
@app.get("/time/{time}/{word}")
async def root(time: int, word:str, background_task: BackgroundTasks):

    # set correct task name based on the way you run the example
    eta = datetime.utcnow() + timedelta(seconds=time)
    res = test_celery.apply_async([word],eta=eta)
    print(res)
    background_task.add_task(background_on_message, res)

    return {"message": "Executed"}



@app.get("/remind_me/{rrule}/{word}")
async def root(rrule: str, word:str, background_task: BackgroundTasks):

    rrule_str = rrulestr(rrule)
    task_id = TaskScheduler.schedule(
            func=test_celery,
            description='Test task',
            args=[word],
            rrule_string=rrule,
        )
    print(task_id)
    background_task.add_task(background_on_message, task_id)

    return {"message": "Executed"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)