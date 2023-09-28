import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input("what date would u like to travel to! (YYYY-MM-DD) - ")
year = date.split("-")[0]
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

song_chart_data = soup.select("li #title-of-a-story")
song_names = [songs.getText(strip=True) for songs in song_chart_data]

# SPOTIFY API

spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
spotify_client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
redirect_uri = os.environ["REDIRECT_URI"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret,
                                               redirect_uri=redirect_uri, scope='playlist-modify-private',
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

songs_uris = []
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
    except:
        print("Error 404 occurred!")
    else:
        try:
            uri = result["tracks"]["items"][0]["uri"]
            songs_uris.append(uri)
        except:
            print("Song not on spotify, skipped!")

playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False,
                                   collaborative=False, description=f"Billboard Hot 100 on {date}")
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=songs_uris)
