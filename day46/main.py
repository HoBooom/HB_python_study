import requests
import os
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pprint import pprint

inputDate = "2000-08-12"

queries = []

music_chart_response = requests.get(f"https://www.billboard.com/charts/hot-100/{inputDate}")
music_chart_soup = BeautifulSoup(music_chart_response.text, "html.parser")

song_names_spans = music_chart_soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

for song in song_names:
    queries.append(f"track: {song} year: 2000")
#print(song_names)
#pprint(queries)

#-------------------------------------------------------------------------------------

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.environ.get("SPOTIFY_CLIENT_URL")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="playlist-modify-private playlist-modify-public",
                                               show_dialog=True,
                                               cache_path=".cache"
                                               ))

user = sp.current_user()
user_id = user["id"]
#print(user_id)


track_uris = []
for query in queries:
    result = sp.search(q=query, type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    except IndexError:
        print(f"No track found for query: {query}")
#pprint(track_uris)

#--------------------------------------------------------------
make_playlist = sp.user_playlist_create(user=user_id, name="2000-08-12 Billboard 100", public=False, description="Billboard Hot 100 from 2000-08-12")
playlist_id = make_playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
# results = sp.artist_albums(taylor_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = sp.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])

#inputDate = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")

# music_chart_song = []
# music_chart_singer = []
#
# list_set = music_chart_soup.find_all(name="li", class_="o-chart-results-list__item")
#
# for item in list_set:
#     song_tag = item.find(name="h3", class_="c-title")
#     artist_tag = item.find(name="span", class_="c-label")
#     if song_tag:
#         music_chart_song.append(song_tag.get_text(strip=True))
#         music_chart_singer.append(artist_tag.get_text(strip=True))

# for i in range(len(music_chart_song)):
#     print(f"{i + 1}) {music_chart_song[i]}\n{music_chart_singer[i]}\n")


