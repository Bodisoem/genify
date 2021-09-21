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
## Sign up for Spotify Developer Account
1. Login or Sign Up: [Spotify Dashboard](https://developer.spotify.com/dashboard/login)
2. When creating a New App, make sure you know your Client ID and Client Secret.
3. Learn more about Spotify APIs at [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## Sign up for Genius APIs
For this project, we only use one-time generate access token from Genius APIs:
1. Fill up information in [Genius APIs Client management page](https://genius.com/api-clients) - you can choose random websites for test purposes.
2. Make sure you hit the **Generate Access Token** button and include it with the Spotify info above value into the .env file (which we will go on later).

## Cloning and some important files
Clone this repo and download all the packages inside requirements.txt
```sh
$ git clone https://github.com/Bodisoem/genify.git
$ cd genify/
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
