FROM python:3-slim
ADD requirements.txt /app/requirements.txt
ADD . /app/
RUN pip install -r app/requirements.txt
#ENTRYPOINT celery -A app.test_celery worker --loglevel=DEBUG
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']