import movie
import fav_movies
from urllib2 import Request, urlopen, URLError
import json
import urllib

abc=[]
i=0
while(i<3):
    title =raw_input('Type in your favourite movie ')
    request = Request('http://www.omdbapi.com/?s='+urllib.quote_plus(title))
    try:
        response = urlopen(request)
        data = response.read()
        d=json.loads(data)
        poster=d['Search'][0]['Poster']
        abc.append(movie.Movie(title, poster))
    except URLError:
        print("Error")
    i=i+1
for fav in abc:
    print(fav.poster)



