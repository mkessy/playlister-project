from django.db import models
from django.test import TestCase
from songs.models import Song
from playlists.models import Playlist


class SongModelTest(TestCase):

    fixtures = ['318_playlist.json', '423_playlist.json',
            '318_songs.json', '423_songs.json']

    def setUp(self):
        Playlist.objects.get(playlistid=423)
        Playlist.objects.get(playlistid=318)

    def test_list(self):
        test_songs_1 = Playlist.objects.get(playlistid=423).songs.all()
        test_songs_2 = Playlist.objects.get(playlistid=318).songs.all()

        album_default = Song._meta.fields[1].default
        artist_default = Song._meta.fields[4].default
        genre_default = Song._meta.fields[7].default
        title_default = Song._meta.fields[2].default

        for song in test_songs_1:
            self.assertTrue(song.album != album_default)
            self.assertTrue(song.artist != artist_default)
            self.assertTrue(song.genre != genre_default)
            self.assertTrue(song.title != title_default)
            self.assertTrue(song.cover_url != "")
            self.assertTrue(song.duration != None)

        for song in test_songs_2:
            self.assertTrue(song.album != album_default)
            self.assertTrue(song.artist != artist_default)
            self.assertTrue(song.genre != genre_default)
            self.assertTrue(song.title != title_default)
            self.assertTrue(song.cover_url != "")
            self.assertTrue(song.duration != None)






