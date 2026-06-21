# import requests
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.title.text)



import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/news")
def get_news():

    url = "https://indianexpress.com/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    soup = BeautifulSoup(response.text, "html.parser")

    titles = []

    for item in soup.find_all("a", class_="topblockNews"):
        titles.append(item.get_text(strip=True))

    return {"news": titles}