from celery import Celery

celery = Celery(
    "tasks",
    broker='amqp://root:example@127.0.0.1:5672'
)
