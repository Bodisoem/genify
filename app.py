import os

from flask import Flask, render_template
from spotify import get_releases, get_top_tracks, get_access_token

ARTIST_ID = ['2hlmm7s2ICUX0LVIhVFlZQ','6LuN9FCkKOj5PcnpouEgny', '3diftVOq7aEIebXKkC34oR']
ARTIST_NAME =['Khalid', 'Gunna', 'Tlinh']

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    
    artist_tracks = {}
    count = 0
    for artist in ARTIST_ID:
        artist_tracks[ARTIST_NAME[count]] = get_top_tracks(artist, get_access_token())
        count +=1
        
    print(artist_tracks)
    return render_template(
        "index.html",
        artist_tracks=artist_tracks
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)