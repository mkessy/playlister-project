#admin interface for model Playlist

from django.contrib import admin
from playlists.models import Playlist, Group, Category

admin.site.register(Playlist)
admin.site.register(Group)
admin.site.register(Category)

