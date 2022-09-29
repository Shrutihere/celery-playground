from celery import Celery

celery = Celery('worker', backend='rpc://', broker='pyamqp://guest@localhost//')

celery.conf.task_routes = {
        "worker.celery_worker.test_celery": "test-queue"}

celery.conf.update(task_track_started=True)

# @app.task
# def scheduler(x, y):
#     return x + y

# ----------command to start worker----------
# celery -A tasks worker -l info -P eventlet