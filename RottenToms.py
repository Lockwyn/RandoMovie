import requests
from bs4 import BeautifulSoup

def scrapUrl(url):
    movies = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h2=soup.find_all("td")
    for h in h2:
        entry=h.find("a").text.split("(")
        if len(entry)>1:
            movies.append({'title': entry[0].strip(),'year': entry[1]})
        else:
            movies.append( {'title': entry[0].strip(), 'year': "NA"} )
    return movies


def fetchMovies(urls):
    movies=[]
    for url in urls:
        movies=movies+scrapUrl(url)
    return movies

def process():
    urls = [
        "https: // www.rottentomatoes.com / top / bestofrt /"
    ]
    return fetchMovies(urls)