import tweepy
# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)

from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'python'
max_tweets = 1000
searched_tweets = [status for status in tweepy.Cursor(
    api.search, q=query).items(max_tweets)]
