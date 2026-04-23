import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

date = input("what year you would like to travel to in YYYY-MM-DD format :")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent":"Chrome/147.0.7727.102",}

response = requests.get(URL,headers= header) 
response.raise_for_status
html_website = response.text

soup = BeautifulSoup(html_website, "html.parser")

song_names_spans = soup.select("li ul li h3")
songs = [ song.getText().strip() for song in song_names_spans ]
# print(songs)

yt = YTMusic(".//music_timemachine//browser.json")

playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

playlist_id = None
playlists = yt.get_library_playlists(limit=100)

PLAYLIST_NAME = "0210"
for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This Playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        "Birthday",
        privacy_status= "UNLISTED", 
    )
    print("Playlist created successfully")

for song in songs:
    try:   
        song_id = yt.search(
        song,
        filter="songs",
        limit=1   
        )
        # print(song_id)
        yt.add_playlist_items(
            playlist_id,
            [song_id[0]["videoId"]],
            duplicates= False    
            )
        print("Song Added")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")