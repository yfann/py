import asyncio
import httpx
from fastapi import FastAPI

app = FastAPI()



@app.get("/slow_data")
async def fetch_data():
    await asyncio.sleep(5) 
    return {"data": "slow data"}


