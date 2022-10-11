# task-scheduler
A short description of this repository goes here

## Local Setup - Development
Install rabbitmq : `sudo apt-get install rabbitmq-server` <br />
Install celery : `pip install celery` <br />
Run the celery worker server : `celery -A tasks worker --loglevel=INFO` <br />
For specific queue : `celery -A app.worker.celery_app worker --loglevel=info -Q test-queue` <br />
Run celery beat : `celery -A app.worker.celery_app beat --loglevel=INFO -s celery_file` <br />
<br />
Run celery server using Flower : `celery -A app.worker.celery_app flower --port=5555` <br />
Url to Flower : `http://localhost:5555/dashboard` <br />
<br />
Run main.py for endpoints<br />
 
## Dockersizing - Production
Build docker image : `docker-compose build` <br />
Run image : `docker-compose up` -d <br />
See logs : `docker-compose logs` -f<br />
List of running containers : `docker container ls` <br />
Stop a server : `docker stop <.container_id.>` <br />

## Celery Concepts
Tasks can be scheduled in two ways :<br />
`send_tasks` - uses 'task_name' to add task to the queue<br />
`apply_async` - uses function name; can provide 'eta' as time for execution<br />
celery beat used for scheduling recurring tasks (check celery_app.py). Next step: make it dynamic <br />



## Flow

### User Flow
<<For laypersons/ testers/ frontend teams>>

### Data Flow
For backend developers to understand how remind me works end to end
