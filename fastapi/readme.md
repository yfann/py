

uvicorn server2:app --host 0.0.0.0 --port 8088 --reload
uvicorn server:app --host 0.0.0.0 --port 8000 --reload


curl -N http://127.0.0.1:8000/stream --no-buffer --noproxy localhost

## tips
+ 需要关闭windows网络代理