from django.db import models
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.db.models.fields import NOT_PROVIDED
from playlists.models import Playlist

BASE_STATION = 'http://songza.com/api/1/station/%s'
BASE_COVER_URL = 'http://songza.com/api/1/station/%s/image'


class PlaylistModelTest(TestCase):

    fixtures = ['318_playlist.json', '423_playlist.json',
            '318_songs.json', '423_songs.json']

    def setUp(self):
        Playlist.objects.get(playlistid=423)
        Playlist.objects.get(playlistid=318)

    def test_list(self):
        test_playlist_1 = Playlist.objects.get(playlistid=318)
        test_playlist_2 = Playlist.objects.get(playlistid=423)

        #Did all the songs get loaded into the playlist?
        self.assertEquals(len(test_playlist_1.songs.all()), 137)
        self.assertEquals(len(test_playlist_2.songs.all()), 61)

        #Did the cover_url field get assigned?
        self.assertEquals(test_playlist_1.cover_url,
                BASE_COVER_URL % test_playlist_1.playlistid)
        self.assertEquals(test_playlist_2.cover_url,
                BASE_COVER_URL % test_playlist_2.playlistid)

        creator_default = test_playlist_1._meta.fields[2]
        self.assertTrue(test_playlist_1.creator != creator_default)
        self.assertTrue(test_playlist_2.creator != creator_default)

        #Did the description field get assigned?
        desc_default = test_playlist_1._meta.fields[5]
        self.assertTrue(test_playlist_1.description != desc_default)
        self.assertTrue(test_playlist_2.description != desc_default)

        #Did the songza_url field get assigned?
        self.assertEquals(test_playlist_1.songza_url,
                BASE_STATION % test_playlist_1.playlistid)
        self.assertEquals(test_playlist_2.songza_url,
                BASE_STATION % test_playlist_2.playlistid)

        spotify_url = "http://spotify.com"
        #Did the spotify_url field get assigned?
        self.assertTrue(test_playlist_1.spotify_url == spotify_url)
        self.assertTrue(test_playlist_2.spotify_url == spotify_url)

        #alternate way, check that fields aren't
#        for field in test_playlist_1._meta.fields:










