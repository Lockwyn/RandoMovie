import requests
from bs4 import BeautifulSoup

def scrapUrl(url):
    movies = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h3=soup.find_all("h3",{'class':'lister-item-header'})
    for h in h3:
        title=h.find("a").text
        year=h.find("span",{'class':'lister-item-year'}).text.strip()
        movies.append({'title': title, 'year': year})
    return movies



def fetchMovies(urls):
    movies=[]
    for url in urls:
        movies=movies+scrapUrl(url)
    return movies

def process():
    urls = [
        "https://www.imdb.com/list/ls068082370/",
        "https://www.imdb.com/list/ls068082370/?page=2",
        "https://www.imdb.com/list/ls068082370/?page=3",
        "https://www.imdb.com/search/title/?genres=fantasy&groups=top_250&sort=user_rating,desc"
    ]
    return fetchMovies(urls)