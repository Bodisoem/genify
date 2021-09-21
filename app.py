import os

from flask import Flask, render_template, redirect, request
from requests.api import post
from spotify import get_top_tracks, get_access_token, get_new_releases
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



ARTIST_ID = ['4O15NlyKLIASxsJ0PrXPfz','06HL4z0CvFAxyc27GXpf02', '699OTQXzgjhIYAHMy9RyPD']
ARTIST_NAME =['Lil Uzi Vert', 'Taylor Swift', 'Playboi Carti']

SPOTIFY_ACCESS_TOKEN=get_access_token()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# app.config['SECRET_KEY'] = 'genify'


# class MyForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])

@app.route('/')
def hello_world():
    # Get data of artist's top track and lyrics links from genius
    artist_tracks = {}
    count = 0
    for artist in ARTIST_ID:
        artist_tracks[ARTIST_NAME[count]] = get_top_tracks(artist, SPOTIFY_ACCESS_TOKEN)
        count +=1

    # Get some new release songs and fetch it lyrics from Genius
    new_releases = get_new_releases(SPOTIFY_ACCESS_TOKEN)

    return render_template(
        "index.html",
        artist_tracks=artist_tracks,
        new_releases=new_releases
    )

# @app.route('/create', methods=['GET','POST'])
# def name():
#     name = None
#     form = MyForm()
#     # Validate Form
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.date = ''
#     return render_template('results.html', name=name, form=form)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
