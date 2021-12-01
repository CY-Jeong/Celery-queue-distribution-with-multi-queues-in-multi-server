from test_celery import celery

second = 5
queue = ""

celery.send_task(
    "task.delay_sec",
    kwargs=second,
    queue=queue_name
)