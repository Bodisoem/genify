from typing import final
from flask.scaffold import F
import requests
import os
from dotenv import find_dotenv, load_dotenv, main
from requests.models import Response
from genius import get_song_info
import base64

# Get client's id and secret key from spotify and access token from genius
load_dotenv(load_dotenv())
SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

AUTH_URL = 'https://accounts.spotify.com/api/token'
ENDPOINTS_NEW_RELEASE = "https://api.spotify.com/v1/browse/new-releases"
ENDPOINTS_SEARCH_ARTIST = "	https://api.spotify.com/v1/search"

GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

# Encode string CLIENT_ID:CLIENT_SECRET using base64
message = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
messageBytes = message.encode('ascii')
base64_bytes = base64.b64encode(messageBytes)
base64_id = base64_bytes.decode('ascii')

# get access token
def get_access_token():
    try:
        # POST
        auth_response = requests.post(AUTH_URL, 
            headers={
                "Authorization" : f"Basic {base64_id}"
                },
            data={
                "grant_type":"client_credentials"
                }
        )
        auth_response.raise_for_status()
        # return the access token
        return auth_response.json()['access_token']
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    


def get_releases(token):
    # GET
    response = requests.get(ENDPOINTS_NEW_RELEASE, 
        headers={"Authorization": f"Bearer {token}"})

    json_res = response.json()
    try:
        for i in range(11):
            print(json_res['albums']['items'][i]['name'])
    except KeyError:
        print("Couldn't get newest releases")

def get_top_tracks(artist_id, token):
    try:
        #GET
        response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks',
            headers={"Authorization": f"Bearer {token}"},
            params={
                'market':'US'
            })
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    else:
        track = []
        for i in range(4):
            dict = {}
            dict['name'] = response.json()['tracks'][i]['name']
            dict['path'] = get_song_info(GENIUS_ACCESS_TOKEN, response.json()['tracks'][i]['name'])[0]
            dict['id'] = response.json()['tracks'][i]['id']
            track.append(dict)
    finally:
        print('Cleaning up, get_top_tracks() irrespective of any exceptions.')
        return track

# Get 5 random artists from spotify
def get_new_releases(token):
    try:
        #GET
        response = requests.get(ENDPOINTS_NEW_RELEASE,
        headers={"Authorization": f"Bearer {token}"},
        params={
            'limit':'5'
        }
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    else:
        new_releases = []

        for i in range(5):
            # track dictionary store a track's Spotify name + id, and Genius path + id to get embeded script from both platforms.
            track = {}

            spotify_response = response.json()['albums']['items']

            track['name'] = spotify_response[i]['name']
            track['spotify_id'] = spotify_response[i]['id']
            track['type'] = spotify_response[i]['type']
            genius_song_info = get_song_info(GENIUS_ACCESS_TOKEN, response.json()['albums']['items'][i]['name'])
            track['genius_path'] = genius_song_info[0]
            track['genius_id'] = genius_song_info[1]
            new_releases.append(track)
    finally:
        print('Cleaning up, get_new_release() irrespective of any exceptions.')
        return new_releases

def search_for_artist(name, token):
    try:
        #GET
        artist_info = requests.get(ENDPOINTS_SEARCH_ARTIST,
        headers={"Authorization": f"Bearer {token}"},
        params= {
            'q' : name,
            'type': 'artist',
            'market': 'US',
            'limit': 1,
        })

        artist_info.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    finally:
        print('Cleaning up, search_for_artist() irrespective of any exceptions.')
        return artist_info.json()['artists']['items'][0]['id']

