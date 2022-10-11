# task-scheduler
## Steps to setup
Install rabbitmq : sudo apt-get install rabbitmq-server<br />
Install celery : pip install celery

## Execution [ locally ]
Run the celery worker server : celery -A tasks worker --loglevel=INFO <br />
For specific queue : celery -A app.worker.celery_app worker --loglevel=info -Q test-queue <br />
Run celery beat : celery -A app.worker.celery_app beat --loglevel=INFO -s celery_file<br />
<br />
Run celery server using Flower : celery -A app.worker.celery_app flower --port=5555<br />
Url to Flower : http://localhost:5555/dashboard<br />
<br />
Run main.py for endpoints<br />
 
## Execution using Docker commands 
Build docker image : docker-compose build<br />
Run image : docker-compose up -d <br />
See logs : docker-compose logs -f<br />
List of running containers : docker container ls<br />
Stop a server : docker stop <.container_id.><br />

## Points to note
Tasks can be scheduled in two ways :<br />
send_tasks - uses 'task_name' to add task to the queue<br />
apply_async - uses function name; can provide 'eta' as time for execution<br />
celery beat used for scheduling recurring tasks (check celery_app.py). Next step: make it dynamic <br />



## References

### Celery Tutorials
[JetBrains Example](https://www.jetbrains.com/pycharm/guide/tutorials/fastapi-aws-kubernetes/redis_celery/)
[Serving ML Models](https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db)
[Async Architecture with FastApi Celery and RabbitMQ](https://medium.com/cuddle-ai/async-architecture-with-fastapi-celery-and-rabbitmq-c7d029030377)
[fullstackpython:celery](https://www.fullstackpython.com/celery.html)

### Python Documentation
[Concurrent Features](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures)
[subprocess](https://docs.python.org/3/library/subprocess.html)
[Event loop](https://docs.python.org/3.9/library/asyncio-eventloop.html#)
[scheduler](https://docs.python.org/3/library/sched.html)
[queue](https://docs.python.org/3/library/queue.html)
[threading](https://docs.python.org/3/library/threading.html#module-threading)
[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
[multiprocessing:shared_memory](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
[futures](https://docs.python.org/3/library/asyncio-future.html)
