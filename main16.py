#cors handling

from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 

app=FastAPI()

# Allowed Origin (front-end url)

origin={
    "http://localhost:5173"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get("/")
def home():
    return {"message":"Hello world from Fastapi  vern"}