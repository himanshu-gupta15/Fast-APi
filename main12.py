# sync and async code 

import time 
import asyncio 
from fastapi import FastAPI 

app=FastAPI() 

@app.get("/")
async def home():
    await asyncio.sleep(2)
    return {
        "message":"Async API"
    }


# def task():
#     time.sleep(2)
#     return "Done"

# async def task_async():
#     await asyncio.sleep(2)
#     return "Done"
