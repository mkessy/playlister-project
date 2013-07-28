from django.db import models
from django.test import TestCase
from songs.models import Song


class SongModelTest(TestCase):

    fixtures = ['318_playlist.json', '423_playlist.json',
            '318_songs.json', '423_songs.json']

    def setUp(self):
        Playlist.objects.get(playlistid=423)
        Playlist.objects.get(playlistid=318)

    def test_list(self):





