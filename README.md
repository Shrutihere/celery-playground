# task-scheduler
This repository contains the endpoints to schedule a task (Edvora Notification) at a specific time or repeating in a pattern based on the RRules.

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
### Introduction
Celery is generally used as a task queue to run the tasks asynchronously, we use it for scheduling (repeating) jobs that are to be run at a (list of) date(s) in future. <i> Celery Architecture </i> <br />
Web (Fastapi): Provide APIs to receive requests.<br />
Broker (RabbitMQ) : A queue for scheduled jobs.<br />
Worker : Servers which pick up tasks to be executed.<br />
Results Backend : To store the task results.<br />
<br /> 
<i> RabbitMQ is an open source message broker - an intermediary for messaging. Celery is a Task Queue software which uses RabbitMQ as a broker to know the status of the tasks in progress </i> <br /> 

### Integration with FastAPI Server
The fastapi app receives the request<br /> 
### Scheduling and Executing jobs
Explain how that works here in some more detail <br /> 


## Flow

### User Flow
<<For laypersons/ testers/ frontend teams>>

### Data Flow
For backend developers to understand how remind me works end to end
