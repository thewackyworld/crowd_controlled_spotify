import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import django 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easyread_project.settings")
django.setup()

from musiclist.models import songitem

# initialize the Spotify object with your credentials and the required scopes
cid, secret, redirect_uri  = '57c03aafe9d146dc936a54b812dab788', 'cbba1a56b1d145088c8fce12de515ee5', 'http://localhost:8888/callback';
scope = 'user-read-playback-state user-modify-playback-state';
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_uri, scope=scope));


def Arrange_song(x):
    x = x.sort_values(by="Vote", ascending=False)
    x = x.reset_index(drop=True)
    return x;


def Time_left():
    current_playback = sp.current_playback();
    remaining_timez = current_playback['item']['duration_ms'] - current_playback['progress_ms']
    return remaining_timez;


def Add_song(song):
    song_name = song['Name'][0]
    artist_name = song['Artist'][0]
    song_id = song['ID'][0]
    print(song_name)

    query = f'track:{song_name} artist:{artist_name}'
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        song_uri = results['tracks']['items'][0]['uri']
        sp.add_to_queue(song_uri)
    else:
        print("song name wrong")
        song = song.drop(0)
        end = songitem.objects.get(id = song_id)
        end.delete()
        Add_song(grab_song())
    song = song.drop(0)
    end = songitem.objects.get(id = song_id)
    end.delete()
    print("Adding To Queue")
    time.sleep(10)

def grab_song():
    objects = songitem.objects.all()
    df = pd.DataFrame(columns=["Name", "Artist" ,"Vote", "ID"]);

    y = 0;
    for obj in objects:
        df.loc[y] = [obj.songname, obj.artist, obj.votes, obj.id]
        y+=1;
        
    df = Arrange_song(df);
    song = df
    print(song)
    return(song)


x = 0;
i = 0;

while x == 0:
    grab_song();
    from musiclist.models import songitem
    current_playback = sp.current_playback();

    if current_playback is not None and current_playback['is_playing']:
        remaining_time = Time_left();

        while remaining_time > 10000:
            remaining_time = Time_left();
            print(remaining_time)
            song = Arrange_song(grab_song());

        if remaining_time <= 10000:
            try:
                Add_song(grab_song())
                i+=1;

            except KeyError:
                print("#######no song in list######")
    else:
        print("Play Music first")
