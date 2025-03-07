import asyncio
import random

async def data_task():
    """
    将原生成器函数封装为异步任务的方法
    """
    async def task_wrapper():
        await asyncio.sleep(random.uniform(5, 10))  # 模拟异步操作
        return 'data'
    
    return await task_wrapper()



async def loop():
    task = asyncio.create_task(data_task()) 
    while True:
        if task.done():
             result = task.result()
             yield result
             task = asyncio.create_task(data_task()) 
        yield 'ping'
        await asyncio.sleep(2)


async def data_slow():
    for i in range(5):
        await asyncio.sleep(3)  # 模拟异步操作
        yield f'data {i}'

async def data_fast():
    while true:
        await asyncio.sleep(1)  # 模拟异步操作
        yield f'data {i}'

async def loop2():
    async for item in data():
        yield item

async def main():
    async for item in loop2():  # 异步迭代
        print(item)

asyncio.run(main())
