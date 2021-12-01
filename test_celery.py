from celery import Celery
from kombu import Queue

celery = Celery(
    "tasks",
    broker='amqp://root:example@rabbitmq:5672'
)
celery.conf.task_queues = (
    Queue('server1', routing_key='server1'),
    Queue('server2', routing_key='server2'),
    Queue('server3', routing_key='server3')
)
