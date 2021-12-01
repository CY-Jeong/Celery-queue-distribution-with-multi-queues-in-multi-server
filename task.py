from .test_celery import celery
import time

@celery.shared_task(bind=True)
def delay_sec(num: int):
    print(f" waiting {num} seconds...")
    print(f" waiting {num} seconds...")
    time.sleep(num)
    print("done")
    print("done")
    

