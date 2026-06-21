# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# data = response.json()

# print(data[:2])

from urllib import response

from fastapi import FastAPI 
import requests 

app=FastAPI()

# GET ALL data 
@app.get("/posts")
def get_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

# Get single post 

@app.get("/posts/{post_id}")
def get_post(post_id:int):
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    # return response.json()

    if response.status_code !=200:
        return {"message":"Post not found"}
    return response.json()