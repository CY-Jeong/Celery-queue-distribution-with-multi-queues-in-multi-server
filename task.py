from .test_celery import celery

@celery.shared_task(bind=True)
def delay_sec(num: int):
    print(f" waiting {num} seconds...")
    