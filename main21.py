import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/news")
def get_news(page:int=1, limit:int=5):

    url = "https://www.jalopnik.com/2194443/which-2021-ev-has-depreciated-most-over-five-years/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    soup = BeautifulSoup(response.text, "html.parser")

    titles = []

    for item in soup.find_all("a", class_="topblockNews"):
        titles.append(item.get_text(strip=True))

    return {"news": titles}