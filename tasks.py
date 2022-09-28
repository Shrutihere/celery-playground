from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def scheduler(x, y):
    return x + y

# ----------command to start worker----------
# celery -A tasks worker -l info -P eventlet