FROM python:3-slim
ADD requirements.txt /app/requirements.txt
ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A test_celery worker --loglevel=info
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']