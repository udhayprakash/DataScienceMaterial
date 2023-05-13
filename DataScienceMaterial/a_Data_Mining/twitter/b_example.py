import tweepy
from textblob import TextBlob

# Authenticate with Twitter API
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Define Twitter handles to analyze
twitter_handles = ["@handle1", "@handle2", "@handle3"]

# Loop through each handle and analyze sentiment of their recent tweets
for handle in twitter_handles:
    print("Analyzing tweets for", handle)
    public_tweets = api.user_timeline(screen_name=handle, count=100)

    # Analyze sentiment of each tweet
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
