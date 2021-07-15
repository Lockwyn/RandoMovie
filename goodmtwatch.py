import requests
from bs4 import BeautifulSoup
import random
urls=[
    "https://agoodmovietowatch.com/netflix/23-best-netflix/"
]
def scrapUrl_Gmtw(url):
    movies = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h2=soup.find_all("h2")
    for h in h2:
        entry=h.find("a").text.split("(")
        movies.append({'title': entry[0].strip(),'year': entry[1]})
    return movies
urls=[
    "https://agoodmovietowatch.com/netflix/23-best-netflix/"
]


print(scrapUrl_Gmtw(urls[0]))
