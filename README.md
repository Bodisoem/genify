# The Genify Web App

An user-friendly web application that allows users to see their favorite artists' songs on Spotify and links to their lyrics on Genius.
**Genify = Genius + Spotify**
Please visit [The Genify Web](https://rocky-ocean-53591.herokuapp.com/) for more info.

## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/) and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) in your working directory.

Login to your heroku account using this command.
```sh
$ heroku login -i
```


Clone this repo and download all the packages inside requirements.txt
```sh
$ git clone https://github.com/csc4350-f21/project1-dvu11.git
$ cd project1-dvu11/
$ pip install -r requirements.txt
```

Create .env file which contain your Spotify Client ID, Client Secret, and Genius Access Token. Format of the file should look like this
```sh
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"

export GENIUS_ACCESS_TOKEN="your_genius_access_token"
```
## Deploy the app
Now create your heroku app with
```sh
$ heroku create
$ git add --all
$ git commit -m 'my first app'
$ git push heroku master
```


### Notes from developer
This app is not finish yet, I try to make search feature where user can look for an random song from their input artist's name. This process demand a good amount of Flask knowledge. Currently, I am trying FlaskWTF (wtforms) which can handle user input. Then I will use the [Spotify API](https://developer.spotify.com/documentation/web-api/).
Specially the Search for Item API in order to get artist id and print out his/her top track.
```sh
  GET https://api.spotify.com/v1/search
```
