from haystack import indexes
from playlists.models import Playlist

class PlaylistIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    featured_artists = indexes.CharField(model_attr='featured_artists')
    pub_date = indexes.CharField(model_attr='date')

    def get_model(self):
        return Playlist

#    def index_queryset(self, using=None):
#        """Used when the entire index for model is updated"""
#        return self.get_model().objects.all()
#
