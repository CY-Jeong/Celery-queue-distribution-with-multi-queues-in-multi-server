from celery import shared_task
import time

@shared_task(bind=True)
def delay_sec(self, *args, **kwargs):
    num = kwargs["num"]
    print(f" waiting {num} seconds...")
    print(f" waiting {num} seconds...")
    time.sleep(num)
    print("done")
    print("done")
    

