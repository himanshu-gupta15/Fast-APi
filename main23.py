# API RATE LIMITING


from fastapi import FastAPI, Request
from slowapi import Limiter 
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse 

app=FastAPI()

# Limiter setup 

limiter=Limiter(key_func=get_remote_address)
app.state.limiter=limiter 

#Error handle 
@app.exception_handler(RateLimitExceeded)
def rate_limit_hander(request:Request,exc:RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail":"Too many Requests"
        }
    )

# Rate limiter api 
@app.get("/data")
@limiter.limit("5/minute")
def get_data(request:Request):
    return {
        "message": "Data retrieved successfully"
    }