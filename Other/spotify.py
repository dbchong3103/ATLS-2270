import sys
from time import time
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import numpy as np
import csv
from sklearn.cluster import KMeans
from scipy.spatial import distance
#import lyricsgenius

# ------------------------- SPOTIFY API HOOKIN
#scope = 'user-library-read'
scope = 'user-library-read'

# ------------------------- SPOTIFY API HOOKIN

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id='f2690140b6d049a3a7aa4a0f6d4be012',
          client_secret='b3ddd5dd34db4f37a509d0313ba0c2fa',
          redirect_uri='http://localhost/',    
          scope=scope, open_browser=False))

#Pick an album
album_results = sp.album('https://open.spotify.com/album/42UPwzHW8rhA13t5JJxp09?si=MRcruXJXS2SqKJvIBwGDyA')
print(album_results['artists'][0]['name'])