import requests
from fastapi import FastAPI
import time

app = FastAPI()

cache_data = []
last_fetch = 0

@app.get("/news")
def get_news():
    global cache_data, last_fetch

    if time.time() - last_fetch > 60:
        print("Fetching fresh data")

        url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=YOUR_API_KEY"

        # response = requests.get(url)
        # data = response.json()
        response = requests.get(url)
        data = response.json()

        print(data)  # Debug

        cache_data = [
            {
                "title": article["title"],
                "description": article["description"],
                "source": article["source"]["name"],
                "author": article["author"],
                "url": article["url"],
                "publishedAt": article["publishedAt"]
            }
            for article in data.get("articles", [])
        ]

        last_fetch = time.time()

    else:
        print("Using cache data")

    return {
        "count": len(cache_data),
        "news": cache_data
    }