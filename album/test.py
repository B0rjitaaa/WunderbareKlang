import urllib.request
import json

API_KEY = "c5a08907c127bcc57ea21a4f19c639fc"
url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=c5a08907c127bcc57ea21a4f19c639fc&artist=Cher&album=Believe&format=json"


artist = urllib.request.urlopen(url)

string = artist.read().decode('utf-8')
json_obj = json.loads(string)



print(json_obj['album']['tracks']['track'][1]['artist']['name'])


