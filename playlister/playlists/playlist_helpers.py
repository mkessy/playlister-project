#helper functions for playlists.views

from playlists.models import Playlist, Group, Category
from songs.models import Song

import requests

HEADER = {"User-Agent":
          "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"}

REQUEST_KWARGS = {'headers':HEADER, 'timeout':10.0, 'allow_redirects':False}

def get_new_playlists():
    """Returns a query set of the web new and notable playlists
    this list may be empty.

    Later functionality can be added to also return playlist ids of playlist not
    in the database. These will then be added to some sort of queue where they will
    retrieved according to some predefined task/cronjob type of deal"""

    SONGZA_NEW_URL = 'http://songza.com/api/1/gallery/slug/songza/web-new-and-notable'

    new_playlists = requests.get(SONGZA_NEW_URL, **REQUEST_KWARGS)
    if new_playlists.status_code != 200:
        return []
    else:
        new_playlists = new_playlists.json()

    new_playlists = new_playlists['station_ids']
    new_playlists = Playlist.objects.filter(pk__in=new_playlists)

    return new_playlists

def get_trending_playlists():
    """Returns a query set of the trending playlists on the songza website,
    this list may be empty.

    Later functionality can be added to also return playlist ids of playlists not
    in the database. These will then be added to some sort of queue where they will be
    retrieved according to some predefined task/cronjob type of deal"""

    SONGZA_TRENDING_URL = 'http://songza.com/api/1/chart/name/songza/trending'
    trending_playlists = requests.get(SONGZA_TRENDING_URL, **REQUEST_KWARGS)
    if trending_playlists.status_code != 200:
        return []
    else:
        trending_playlists = trending_playlists.json()

    trending_playlists = [playlist['id'] for playlist in trending_playlists]
    trending_playlists = Playlist.objects.filter(pk__in=trending_playlists)

    return trending_playlists

def get_alltime_playlists():
    """Returns a query set of the most popular all-time playlists"""

    SONGZA_ALLTIME_URL = 'http://songza.com/api/1/chart/name/songza/all-time'
    alltime_playlists = requests.get(SONGZA_ALLTIME_URL, **REQUEST_KWARGS)
    if alltime_playlists.status_code != 200:
        return []
    else:
        alltime_playlists = alltime_playlists.json()
    alltime_playlists = [playlist['id'] for playlist in alltime_playlists]
    alltime_playlists = Playlist.objects.filter(pk__in=alltime_playlists)

    return alltime_playlists

def chunk_list(l, n):
    """returns a list of length x lists given a list l"""

    return [l[x:x+n] for x in xrange(0, len(l), n)]

