
## install celery
+ `pip install celery[redis]`


## docker redis
+ `docker pull redis`
+ `docker run -d --name redis-server --privileged -p 6379:6379 redis`
+ `docker exec -it redis-server redis-cli`
    + `ping`
+ host安装redis-cli
    + `redis-cli -h 127.0.0.1 -p 6379`

## run celery
+ `celery –A server worker –-loglevel=INFO`
+ `python client.py`


## tips
+ `ps aux | grep 'celery'`