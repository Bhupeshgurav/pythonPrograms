import tweepy

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMmzcQEAAAAAwCm74c8088ZWjD1LZPuxReyuvdA%3D8Ax8GUwRaSmvRoslDjXrAPX8VLhMWPfdnmsNkLbs4o6Xp2Qea6"

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "5T4dVw604ywCrhka3aoEFnfj1"
consumer_secret = "J6iiBKUrGdwKdLf8Pjw2yTmVItB03nn2xv0E10RfANglYSLZHt"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = "1441069656911990792-rScPmIBXMUxEKmBzc9wKESGZdrDJEW"
access_token_secret = "mqWewbrvpbuG0toIdo55wpe55DEDaadZwmQKOKDieqBdY"

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
print(dir(client.get_me))
client = tweepy.Client(bearer_token)

# Get Recent Tweets Count

# This endpoint/method returns count of Tweets from the last seven days that
# match a search query

query = "Tweepy -is:retweet"

# Granularity is what you want the timeseries count data to be grouped by
# You can request minute, hour, or day granularity
# The default granularity, if not specified is hour
response = client.get_recent_tweets_count(query, granularity="day")

for count in response.data:
    print(count)


client = tweepy.Client(bearer_token)

# Get User's Tweets

# This endpoint/method returns Tweets composed by a single user, specified by
# the requested user ID

user_id = 2244994945

response = client.get_users_tweets(user_id)

# By default, only the ID and text fields of each Tweet will be returned
for tweet in response.data:
    print(tweet.id)
    print(tweet.text)

# By default, the 10 most recent Tweets will be returned
# You can retrieve up to 100 Tweets by specifying max_results
response = client.get_users_tweets(user_id, max_results=100)
