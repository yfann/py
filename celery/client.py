from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')
app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

def manage_sqrt_task(value):
    result = app.send_task('tasks.sqrt_task', args=(value,))
    print(result.get())

if __name__ == '__main__':
    manage_sqrt_task(4)