# openMovieDL: A simple script to get download links of movies and TV series
# from open directories
# Copyright (C) 2020 Prashant Sengar
# Contact: https://github.com/prashantsengar
# prashantsengar5@gmail.com
from googlesearch import search
import requests
import logging
from bs4 import BeautifulSoup as bs
import urllib

logging.basicConfig(filename="log.txt", filemode="w")

q = "index of " + input("Enter movie name: ")

results = search(q, stop=20, tld="co.in")

links = []
for j in results:
    # If links are from News portals, ignore them
    if any(
        x in j
        for x in [
            "imdb",
            "economictimes",
            "news",
            "money",
            "businesstoday",
            "indiatoday",
            "ndtv",
            "india",
            "koimoi",
        ]
    ):
        continue
    else:
        links.append(j)

logging.info("links: ")
logging.info(links)
logging.info("----")


def get_dl_links(link):
    r = requests.get(link).text
    s = bs(r, "html.parser")
    l = s.find_all("a")

    movieLinks = []
    for li in l:
        if (
            li["href"].lower().endswith(".mkv")
            or li["href"].lower().endswith(".mp4")
            or li["href"].lower().endswith(".flv")
        ):
            movieLinks.append(li["href"])
    return movieLinks


dl_links = []
for link in links:
    try:
        dl_links.extend(get_dl_links(link))
    except Exception as e:
        logging.exception(e)

for link in dl_links:
    print(urllib.parse.unquote(link))
