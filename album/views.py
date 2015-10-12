import urllib.request
import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from album.models import *
from album.forms import *


def index(request):
  # Listar todos los albums que se tengan de momento
  response={
    'albums': Album.objects.all().count(),
    'movies': 0,
  }
  return render(request, 'index.html', response)


def list_my_albums(request):
  response={
    'albums': Album.objects.all().order_by('artist', 'title')
  }
  return render(request, 'list-albums.html', response)


def show_album(request, album_id):
  response = {
    'album': Album.objects.get(pk=album_id)
  }
  return render(request, 'album.html', response)


def local_search(request):
  response = {}
  if request.method == 'POST':
    local_search = request.POST.get('local-search')
    albums = Album.objects.filter(artist__icontains=local_search)
    if len(albums)>0:
      response={
      'albums': albums
      }
      return render(request, 'list-albums.html', response)
    else:
      response={
      'albums': Album.objects.all().count(),
      'movies': 0,
      'error': 'No se ha encontrado ningún resutlado.'
      }
  return render(request, 'index.html', response)

  

def search_lastfm(request):
  response = {}
  if request.method == 'POST':
    album_form = request.POST.get('album-title')
    album_form = album_form.replace(' ','+')
    artirst_form = request.POST.get('artist-name')
    artirst_form = artirst_form.replace(' ', '+')

    # Buscar por ALBUM
    if artirst_form is None or artirst_form == '':
      url = 'https://itunes.apple.com/search?term=' + album_form + '&entity=album'
      response = {
        'artist': True
      }

    # Buscar por ARTISTA
    elif artirst_form and album_form is '':
      url = 'https://itunes.apple.com/search?term=' + artirst_form + '&entity=album'

    # Buscar por ARTISTA y ALBUM
    else:
      url = 'https://itunes.apple.com/search?term=' + artirst_form + '+' + album_form +'&entity=album'

    albums = urllib.request.urlopen(url)
    string = albums.read().decode('utf-8')
    json_obj = json.loads(string)
    response['albums'] = json_obj['results']

    print("coñoo: ", int(json_obj['resultCount']))

    if (int(json_obj['resultCount']))==0:
      response['error'] = 'No se han encontrado resultados para la búsqueda.'
      print("esto que es") 

    return render(request, 'search-album.html', response)

  return render(request, 'search-album.html', response)


def show_artists_albums(request, artist_id):
  url = 'https://api.spotify.com/v1/artists/' + artist_id + '/albums?limit=50&market=ES'
  albums = urllib.request.urlopen(url)
  string = albums.read().decode('utf-8')
  json_obj = json.loads(string)
  test = {}
  aver = []
  for entry in json_obj['items']:
    test['name'] = entry['name']
    test['id'] = entry['id']
    test['image'] = entry['images'][0]['url']
    # Get total tracks
    url_tracks = 'https://api.spotify.com/v1/albums/' + test['id'] +'?limit=50'
    tracks = urllib.request.urlopen(url_tracks)
    string_tracks = tracks.read().decode('utf-8')
    string_obj = json.loads(string_tracks)
    test['numtracks'] = string_obj['tracks']['total']
    aver.append(test)
    test = {}

  response = {
    'albums': aver
  }
  return render(request, 'search-album.html', response)


def add_album (request, album_mbid):
  url = 'https://itunes.apple.com/lookup?id='+ album_mbid +'&entity=song'
  album_request = urllib.request.urlopen(url)
  string = album_request.read().decode('utf-8')
  json_obj = json.loads(string)
  if not Album.objects.filter(reference_code=album_mbid):
    album = Album.objects.create(
        title=json_obj['results'][0]['collectionName'],
        artist=json_obj['results'][0]['artistName'],
        date_published=json_obj['results'][0]['releaseDate'][:10],
        picture=json_obj['results'][0]['artworkUrl100'],
        reference_code=json_obj['results'][0]['collectionId'],
        genuine=True
      )
    album.save()
    i = 1
    while i < json_obj['resultCount']:
      song = Song.objects.create(
        title=json_obj['results'][i]['trackName'],
        duration=json_obj['results'][i]['trackTimeMillis'],
        album=album,
        rank=json_obj['results'][i]['trackNumber']
        )
      song.save()      
      i += 1 
    genre = Genre.objects.create(
        album=album,
        name=json_obj['results'][0]['primaryGenreName']
      )
    genre.save()
    return HttpResponseRedirect(reverse('my-albums'))  
  else:
    print("ya tieens ese album")
  return render(request, 'list-albums.html')


def add_collection_albums(request):
  if request.method == 'POST':
    album_mbids = request.POST.getlist('ids')
    for album_mbid in album_mbids:
      url = 'https://itunes.apple.com/lookup?id='+ album_mbid +'&entity=song'
      album_request = urllib.request.urlopen(url)
      string = album_request.read().decode('utf-8')
      json_obj = json.loads(string)
      if not Album.objects.filter(reference_code=album_mbid):
        album = Album.objects.create(
            title=json_obj['results'][0]['collectionName'],
            artist=json_obj['results'][0]['artistName'],
            date_published=json_obj['results'][0]['releaseDate'][:10],
            picture=json_obj['results'][0]['artworkUrl100'],
            reference_code=json_obj['results'][0]['collectionId'],
            genuine=True
          )
        album.save()
        i = 1
        while i < json_obj['resultCount']:
          song = Song.objects.create(
            title=json_obj['results'][i]['trackName'],
            duration=json_obj['results'][i]['trackTimeMillis'],
            album=album,
            rank=json_obj['results'][i]['trackNumber']
            )
          song.save()      
          i += 1
    response={
      'albums': Album.objects.all()
    }
    return render (request, 'list-albums.html', response)


def add_album_manual(request):
  return render(request, 'custom-add.html')