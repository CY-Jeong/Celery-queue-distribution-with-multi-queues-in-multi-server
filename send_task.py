from test_celery import celery
from task import delay_sec

second = {"num": 5}
queue_name = "server1"

celery.send_task(
    "app.task.delay_sec",
    kwargs=second,
    queue=queue_name
)