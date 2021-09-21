import requests
import os
from dotenv import find_dotenv, load_dotenv

# Get client's id and secret key and URI_LINK
load_dotenv(load_dotenv())
GENIUS_CLIENT_ID=os.getenv("GENIUS_CLIENT_ID")
GENIUS_CLIENT_SECRET=os.getenv("GENIUS_CLIENT_SECRET")
GENIUS_ACCESS_TOKEN=os.getenv("GENIUS_ACCESS_TOKEN")
GENIUS_URI=os.getenv("GENIUS_URI")

AUTHORIZE_LINK="https://api.genius.com/oauth/token"


def get_song_info(access_token, song_name):
    try:
        #GET
        response = requests.get('https://api.genius.com/search',
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        params={
            'q': song_name
        })
        response.raise_for_status()

        song_id =  response.json()['response']['hits'][0]['result']['id']

        search_song = requests.get(f'https://api.genius.com/songs/{song_id}',
        headers={
            'Authorization': f"Bearer {GENIUS_ACCESS_TOKEN}"
        })
        search_song.raise_for_status()

        song_info = search_song.json()

        return song_info['response']['song']['path'], song_info['response']['song']['id']
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

