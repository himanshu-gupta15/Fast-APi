# middleware 

import time

from fastapi import FastAPI, Request 

app=FastAPI()

app.middleware("http") 
async def log_middleware(request:Request,call_next):
    start_time=request.time()
    response=await call_next(request)

    process_time=time.time()-start_time

    print(f"Path:{request.url.path} | Time:{process_time}")

    return response 


# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print("Request Received")
#     response=await call_next(request)

#     print("Response Sent")

    

#     return response