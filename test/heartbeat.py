import asyncio
import random

# async def data_slow(queue):
#     """慢速数据流"""
#     for i in range(5):
#         # await asyncio.sleep(random.uniform(5, 10))  # 随机延迟 5~10s
#         await queue.put(f"data: data {i}\n\n")  # 推送数据
#     await queue.put("data: end\n\n")  # 结束信号

async def keep_alive(queue):
    """心跳消息，防止前端超时"""
    while True:
        # await asyncio.sleep(2)  # 每 2 秒发送一次心跳
        await queue.put("data: heartbeat\n\n")

async def main():
    queue = asyncio.Queue()

    # 并行运行数据流和心跳
    heartbeat_task = asyncio.create_task(keep_alive(queue))
    # slow_task = asyncio.create_task(data_slow(queue))


    # 读取队列数据
    while True:
        data = await queue.get()
        print(data, end="")  # 这里模拟输出到前端 SSE
        if "end" in data:  # 终止条件
            break

    # 取消心跳任务（防止程序无限运行）
    heartbeat_task.cancel()
    try:
        await heartbeat_task
    except asyncio.CancelledError:
        pass

asyncio.run(main())
