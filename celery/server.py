from math import sqrt
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')
app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

@app.task
def sqrt_task(value):
    return sqrt(value)