import urllib
from urllib2 import Request, urlopen, URLError
import json
import movie
import fav_movies
from bs4 import BeautifulSoup

def get_youtube_url(title):
    query = urllib.quote_plus(title+"trailer")
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        youtube_url= 'https://www.youtube.com' + vid['href']
        break
    return youtube_url

def get_poster(title):
    title =raw_input('Type in your favourite movie ')
    omdb_request = Request('http://www.omdbapi.com/?s='+urllib.quote_plus(title))
    response = urlopen(omdb_request)
    data = response.read()
    d=json.loads(data)
    if 'false' in d:
        poster= "No such movie"
    else:
        poster=d['Search'][0]['Poster']
    return poster
    

movies_list=[]
i=0
while(i<3):
    title =raw_input('Type in your favourite movie ')
    movies_list.append(movie.Movie(title, get_poster(title), get_youtube_url(title)))
    i=i+1
    
for fav_movie in movies_list:
    print(fav_movie.poster)
    print(fav_movie.trailer_url)                   



