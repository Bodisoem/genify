import requests
import os
from dotenv import find_dotenv, load_dotenv, main
import base64

# Get client's id and secret key
load_dotenv(load_dotenv())
SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

AUTH_URL = 'https://accounts.spotify.com/api/token'
ENDPOINTS_NEW_RELEASE = "https://api.spotify.com/v1/browse/new-releases"


# Encode string CLIENT_ID:CLIENT_SECRET using base64
message = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
messageBytes = message.encode('ascii')
base64_bytes = base64.b64encode(messageBytes)
base64_id = base64_bytes.decode('ascii')

# get access token
def get_access_token():
    # POST
    auth_response = requests.post(AUTH_URL, 
        headers={
            "Authorization" : f"Basic {base64_id}"
            },
        data={
            "grant_type":"client_credentials"
            }
    )
    # return the access token
    return auth_response.json()['access_token']


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
    #GET
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks',
        headers={"Authorization": f"Bearer {token}"},
        params={
            'market':'US'
        })

    track_ids = []
    for i in range(5):
        track_ids.append(response.json()['tracks'][i]['id'])

    return track_ids
