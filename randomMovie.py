import imdb
import goodmovietowatch
import random
import cache

def fetch():
    movies=[]
    movies=movies+imdb.process()
    movies = movies + goodmovietowatch.process()
    cache.writeCSV(movies)


def recommend(k=3):
    movies=cache.readCSV()
    return random.sample(movies, k)

#movies=fetch()
rec=recommend()
print(rec)

