from fastapi import FastAPI 

app=FastAPI()

@app.get("/")
def home():
    return {"message":"APi testing with Fastapi"}

@app.get("/add")

def add(a:int,b:int):
    return {"result":a+b}