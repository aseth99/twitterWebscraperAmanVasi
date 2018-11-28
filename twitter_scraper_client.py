# twitter:
# Consumer API keys
#(API secret key)

# Access token & access token secret
#(Access token)

# (Access token secret)

# Read and write (Access level)

# https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries

# we gon use tweepy library
# pip install tweepy

# https://12factor.net/config
# we not gona hardcode key and access token in python
# cuz using environment to store config details is language and OS agnostic. Changing config for local doesnt require changes to src
#this file authorizes twitter scraping, import get twitter client from here every time we gona scrape twitter
# so set environment variables
#have set 
# export API_KEY=
# export API_SECRET_KEY=
# export ACCESS_TOKEN=
# export ACCESS_TOKEN_SECRET=
#var api_key = process.env.API_KEY;
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
	#setup twitter authentication
	#return: tweepy.OAuthHandler object

	try:
		consumer_key = os.environ["API_KEY"]
		consumer_secret = os.environ["API_SECRET_KEY"]
		access_token = os.environ["ACCESS_TOKEN"]
		access_secret = os.environ["ACCESS_TOKEN_SECRET"]
	except KeyError:
		sys.stderr.write("TWITTER_* env vars not set\n")
		sys.exit(1)
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	return auth

def get_twitter_client():
	#setup twitter API client
	#return tweepy.API object
	auth = get_twitter_auth()
	client = API(auth)
	return client














