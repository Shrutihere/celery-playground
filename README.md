# task-scheduler
## Steps to setup
Install rabbitmq : sudo apt-get install rabbitmq-server<br />
Install celery : pip install celery

## Execution
Run the celery worker server : celery -A tasks worker --loglevel=INFO <br />
Run test.py and observe celery server for output

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
