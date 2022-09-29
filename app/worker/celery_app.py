from celery import Celery

celery = Celery('worker', backend='rpc://', broker='pyamqp://guest@localhost//')

celery.conf.task_routes = {
        "app.worker.celery_worker.test_celery": "test-queue"}

celery.conf.update(imports=['app.worker.celery_worker'])



# ----------command to start worker----------
# celery -A tasks worker -l info -P eventlet
# celery -A app.worker.celery_app worker --loglevel=info -Q test-queue -P eventlet
# celery -A app.worker.celery_app flower --port=5555