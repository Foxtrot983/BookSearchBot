#https://ru.pdfdrive.com/assets/js/combined.js,qv3.84.pagespeed.jm.3BGFzs7v9X.js

import time
from bs4 import BeautifulSoup
import requests

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
#url = f"https://ru.pdfdrive.com/search?q={obj}&pagecount=&pubyear=&searchin=ru&em=&more=true"
#URL1 = "https://ru.pdfdrive.com/search?q="
#URL2 = "&pagecount=&pubyear=&searchin=ru&em=&more=true"


def get_download_url(url: str):
    response = requests.get(url, headers=HEADERS)


    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find("a", class_="btn-user"))
    pass
    #download_url = href
    #return download_url


if __name__ == "__main__":
    get_download_url("https://ru.pdfdrive.com/Освой-самостоятельно-c-по-одному-часу-в-день-d183944321.html")