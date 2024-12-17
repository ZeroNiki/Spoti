import time

import requests
from bs4 import BeautifulSoup

from src.config import YT_LINK


def yt_search(keyword: str):
    print("Searching...")

    link = f"{YT_LINK}{keyword}"
    print(link)

    r = requests.get(link)
    print("Please wait 3 second")
    time.sleep(3)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        get_buttons = soup.find("div", class_="icon-buttons")
        get_href = get_buttons.find("a")["href"]

        print(get_href)

        return get_href

    else:
        print("Error")
        return None
