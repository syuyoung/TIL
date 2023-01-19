import json
#from pprint import pprint 예쁘게 프린트
with open('data/movie.json' , 'r', encoding='utf8') as f:
    movie = json.loda(f)
    print(movie)
    print(movie['title'])


with open('data/movies.json' , 'r', encoding='utf8') as f:
    movie = json.loda(f)
    print(movie)
    #각 리스트의 요소?
    