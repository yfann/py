import asyncio
import random
import httpx
import logging
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()
url = 'http://localhost:8088/slow_data'

async def data_slow(queue):
    logger.info('data_slow start')
    """慢速数据流"""
    data = await fetch(url)
    logger.info(f"data_slow: {data}")
    await queue.put(data)
    await queue.put('end')  # 结束信号

async def keep_alive(queue):
    """心跳消息，防止 SSE 超时"""
    while True:
        await asyncio.sleep(2)  # 每 2 秒发送一次心跳
        await queue.put("data: heartbeat\n\n")
        logger.info('heartbeat')
    
async def fetch(url):
    logger.info('fetch')
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url)
            response.raise_for_status()  # 检查 HTTP 响应状态
            return response.text
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error occurred: {e}")
    except httpx.RequestError as e:
        logger.error(f"Request error occurred: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    return "error"  # 发生异常时返回 None

async def event_stream():
    queue = asyncio.Queue()

    # 创建数据流和心跳任务
    heartbeat_task = asyncio.create_task(keep_alive(queue))
    slow_task = asyncio.create_task(data_slow(queue))

    try:
        while True:
            data = await queue.get()
            yield data
            if "end" in data:  # 收到结束信号后退出
                break
    finally:
        heartbeat_task.cancel()
        try:
            await heartbeat_task
        except asyncio.CancelledError:
            pass

@app.get("/stream")
async def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")