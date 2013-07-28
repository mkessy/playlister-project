import datetime
import pprint
import simplejson as json
import pytz


# Uitility script to convert raw scraped playlists and songs into django
# serializable models


def playlist_to_model(playlist, songs):
    """Converts a raw playlist (see songza.py) to a file containing
    the playlist and the songs in serializble django format (json)

    This method is intended to be used for creating fixtures for tests
    and other general loading of initial data. The django serializable json
    format is shown below.

        [
          {
            "model": "myapp.person",
            "pk": 1,
            "fields": {
              "first_name": "John",
              "last_name": "Lennon"
            }
          },
          {
            "model": "myapp.person",
            "pk": 2,
            "fields": {
              "first_name": "Paul",
              "last_name": "McCartney"
            }
          }
        ]

    """
    utc = pytz.utc
    thedate = datetime.datetime.now(utc)
    thedate = thedate.__str__()

    #create list of songs in serialized format
    serialized_songs = []
    for song in songs:
        song_model = {
                "model": "songs.Song",
                "pk": song['song']['id'],
                "fields": {
                    "album": song['song']['album'],
                    "artist": song['song']['artist']['name'],
                    "title": song['song']['title'],
                    "cover_url": song['song']['cover_url'],
                    "duration": song['song']['duration'],
                    "genre": song['song']['genre'],
                    "date": thedate
                    }
                }
        serialized_songs.append(song_model)

    song_pks = [song['pk'] for song in serialized_songs]
    serialized_playlist = {
        "model": "playlists.Playlist",
        "pk": playlist['id'],
        "fields": {
            "name": playlist['name'],
            "songs": song_pks,
            "song_count": len(song_pks),
            "creator": playlist['creator_name'],
            "cover_url": playlist['cover_url'],
            "date": thedate,
            "description": playlist['description'],
            "songza_url": playlist['url'],
            "spotify_url": "http://spotify.com",
            }

        }

    return (serialized_playlist, serialized_songs)


def main():

    #open genres stations file, '_curated-pop_station.json' will be used
    #for most tests
    with open('_curated-pop_station.json') as f:
        stations = json.load(f)

    #open stations info file
    with open('station_info.json') as f:
        stations_info = json.load(f)

    #test stations used are #318 and 423 in _curated-pop_station.json
    test_stations = ['318', '423']
    playlists = [stations[station_id] for station_id in test_stations]
    songs = [station['songs'] for station in playlists]
    playlist_info = [stations_info['318'], stations_info['423']]

    playlist_songs = zip(playlist_info, songs)
    playlist_songs = [playlist_to_model(playlist, song)
            for playlist, song in playlist_songs]

    for playlist, songs in playlist_songs:
        with open(str(playlist['pk'])+'_playlist.json', 'w+') as f:
            json.dump([playlist], f)

        with open(str(playlist['pk'])+'_songs.json', 'w+') as f:
            json.dump(songs, f)


if __name__ == '__main__':
    main()









