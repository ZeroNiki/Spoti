from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from time import sleep

from src.config import DRIVER

firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.set_preference("browser.cache.disk.enable", False)
firefox_options.set_preference("browser.cache.memory.enable", False)
firefox_options.set_preference("browser.cache.offline.enable", False)
firefox_options.set_preference("network.http.use-cache", False)
service = Service(f'{DRIVER}')
driver = webdriver.Firefox(options=firefox_options, service=service)


def get_spotify_track(url):
    # Get track name
    print("Get track title")
    driver.get(url)
    span = driver.find_element(By.CLASS_NAME, "rEN7ncpaUeSGL9z0NGQR")

    h1 = span.find_element(
        By.CSS_SELECTOR, "h1.encore-text.encore-text-headline-large.encore-internal-color-text-base")

    track_name = h1.text

    # get author
    print("Get author name")
    author_div = driver.find_element(
        By.CSS_SELECTOR, "div.RANLXG3qKB61Bh33I0r2.NO_VO3MRVl9z3z56d8Lg")
    span_name = author_div.find_element(
        By.CSS_SELECTOR, "span.encore-text.encore-text-body-small-bold")

    name = span_name.find_element(By.TAG_NAME, "a")
    author_name = name.text

    # get album cover
    print("Get album cover")
    cover_div = driver.find_element(By.CLASS_NAME, "CmkY1Ag0tJDfnFXbGgju")
    cover = cover_div.find_element(
        By.CSS_SELECTOR, "img.mMx2LUixlnN_Fu45JpFB.CmkY1Ag0tJDfnFXbGgju._EShSNaBK1wUIaZQFJJQ.Yn2Ei5QZn19gria6LjZj")

    secret = cover.get_property('srcset')
    urls = secret.split(", ")
    cover_url = max(urls, key=lambda x: int(
        x.split(' ')[1][:-1])).split(' ')[0]

    # get album name
    try:
        print("Get album name")
        album_div = driver.find_element(
            By.CLASS_NAME, "encore-text.encore-text-body-small.w1TBi3o5CTM7zW1EB3Bm")
        album_name = album_div.find_element(By.TAG_NAME, "a")
    except Exception:
        print("Album name not found")
        album_name_text = None

    driver.quit()

    return [author_name, track_name, cover_url, album_name_text]
