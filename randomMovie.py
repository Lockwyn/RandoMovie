import imdb
import goodmovietowatch
import random
import cache
import argparse

def fetch():
    movies=[]
    movies=movies+imdb.process()
    movies = movies + goodmovietowatch.process()
    cache.writeCSV(movies)


def recommend(k=3):
    movies=cache.readCSV()
    return random.sample(movies, k)





parser = argparse.ArgumentParser()
parser.add_argument("--fetch", help="build movies database by scrapping the web",action="store_true")
args = parser.parse_args()

if args.fetch:
    fetch()
rec=recommend()
print(rec)

