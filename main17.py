#cors handling

from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from config import settings
import os 
from dotenv import load_dotenv 
app=FastAPI()
load_dotenv()

# Allowed Origin (front-end url)
print(os.getenv("ORIGINS"))
# origin=os.getenv("ORIGINS")
origin=settings.origins
SECRET_KEY=os.getenv("SECRET_KEY")
DB_URL=os.getenv("DB_URL")

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