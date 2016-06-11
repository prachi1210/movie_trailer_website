import urllib
from urllib2 import Request, urlopen, URLError
import json
import movie
import fav_movies

movies_list=[]
i=0
while(i<3):
    title =raw_input('Type in your favourite movie ')
    request = Request('http://www.omdbapi.com/?s='+urllib.quote_plus(title))
    try:
        response = urlopen(request)
        data = response.read()
        d=json.loads(data)
        poster=d['Search'][0]['Poster']
        movies_list.append(movie.Movie(title, poster))
    except URLError:
        print("Error")
    i=i+1
for fav_movie in movies_list:
    print(fav_movie.poster)



