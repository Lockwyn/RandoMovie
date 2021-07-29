import requests
from bs4 import BeautifulSoup



def process():
    movies=[]
    urls = [
        "https://agoodmovietowatch.com/netflix/23-best-netflix/",

    ]
    for url in urls:
        movies=movies+scrapUrl_Gmtw(url)
    return movies

def getUrls():
    n_pages = 10
    base_link = "https://agoodmovietowatch.com/netflix/23-best-netflix/"
    urls = []
    for i in range(1,n_pages+1):
        url=base_link
        if i>1:
            url=base_link+f"page/{i}/"
        urls.append(url)
    return urls


def scrapUrl_Gmtw(url):
    movies = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h2=soup.find_all("h2")
    for h in h2:
        entry=h.find("a").text.split("(")
        if len(entry)>1:
            movies.append({'title': entry[0].strip(),'year': entry[1]})
        else:
            movies.append( {'title': entry[0].strip(), 'year': "NA"} )
    return movies


def process():
    movies=[]
    urls = getUrls()
    for url in urls:
        movies=movies+scrapUrl_Gmtw(url)
    return movies



