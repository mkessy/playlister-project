# Create your views here.

from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from playlists.models import Playlist, Group, Category
from songs.models import Song

import playlist_helpers as helpers

def home(request):
    """View for the home page"""

    # context variables for 'playlister_home.html'
    # header1
    # header1_playlists
    # header2
    # header2_playlists
    # header3
    # header3_playlists

    trending = helpers.get_trending_playlists()
    new = helpers.get_new_playlists()
    alltime = helpers.get_alltime_playlists()

    if trending:
        trending = helpers.chunk_list(trending, 3)
    if new:
        new = helpers.chunk_list(new, 3)
    if alltime:
        alltime = helpers.chunk_list(alltime, 3)

    context_dict = RequestContext(request, {
                    "header1": "trending",
                    "header2": "new and notable",
                    "header3": "all-time popular",
                    "header1_playlists": trending,
                    "header2_playlists": new,
                    "header3_playlists": alltime,
                    })

    return render_to_response('playlister_home.html', context_dict)

def playlist(request, **kwargs):

    # context variables for 'playlist_view.html'
    # playlist
    # similar

    plist = get_object_or_404(Playlist, **kwargs)
    songs = plist.songs.all()
    similar = plist.get_similar()

    if similar:
        similar = helpers.chunk_list(similar, 1)
    else:
        similar = []

    print(type(plist))
    print(type(similar))
    print(similar)
    print(plist.formatted_duration())
    context_dict = RequestContext(request, {"playlist": plist, "playlistsongs":songs, "similar": similar})


    return render_to_response('playlists/playlist_view.html', context_dict)

def category(request, categoryid):

   # context variables for 'playlister_sub_browse_base.html'
   # category
   # category_groups

   cat = get_object_or_404(Category, categoryid=categoryid)
   cat_groups = cat.groups.all()

   context_dict = RequestContext(request, {"category": cat, "category_groups": cat_groups,})

   return render_to_response('playlister_sub_browse_base.html', context_dict)

def group(request, groupid):

    grp = get_object_or_404(Group, groupid=groupid)
    cat = Category.objects.get(groups__groupid__exact=grp.groupid)

    return render_to_response('playlist_group.html',
            RequestContext(request, {"group": grp, "category": cat,}))

def about(request):

    return render_to_response('about.html',
            RequestContext(request, {}))



def trending(request):
    """View for the trending sub-section"""

    # context variables for 'playlister_group.html'
    # group
    # group_name

    trending = helpers.get_trending_playlists()

    if trending is not None:
        trending = helpers.chunk_list(trending, 4)
        return render_to_response('playlist_group.html',
                RequestContext(request, {"group_name": "trending",
                    "group": trending,}))
    else:
        raise Http404


def new(request):
    """View for the new and notable sub-section"""

    new = helpers.get_new_playlists()

    new = helpers.chunk_list(new, 4)
    if new is not None:
        return render_to_response('playlist_group.html',
                RequestContext(request, {"group_name": "new and notable",
                    "group": new,}))
    else:
        raise Http404

def alltime(request):
    """View for the new and notable sub-section"""

    alltime_pop = helpers.get_alltime_playlists()

    alltime_pop = helpers.chunk_list(alltime_pop, 4)

    if alltime_pop is not None:
        return render_to_response('playlist_group.html',
                RequestContext(request, {"group_name": "popular this year",
                "group": alltime_pop,}))
    else:
        raise Http404

