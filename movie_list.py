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
    omdb_request = Request('http://www.omdbapi.com/?s='+urllib.quote_plus(title))
    response = urlopen(omdb_request)
    data = response.read()
    d=json.loads(data)
    if 'False' in data:
        poster= "https://az853139.vo.msecnd.net/static/images/not-found.png" #No image found message
    else:
        poster=d['Search'][0]['Poster']
    return poster
    

movies_list=[]
i=0
print('No of movie trailers you want to view? ')
n=raw_input()
print(n)
while(i<n):
    print('Your favorite movie no '+str(i+1))
    title=raw_input()
    movies_list.append(movie.Movie(title, get_poster(title), get_youtube_url(title)))
    i=i+1
    print(i)
    
                  
fav_movies.open_movies_page(movies_list)
