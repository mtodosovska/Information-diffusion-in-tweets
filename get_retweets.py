import tweepy
import pandas as pd

consumer_token = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def getRetweets(id_tweet, sentiment, tweet_text):

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        retweets = api.retweets(id_tweet)
        tweet = api.get_status(id_tweet)
        faves = tweet.favorite_count
        timestamp = tweet.created_at
        retweet_list = []
        for i in range(0, len(retweets)):
            retweet_list.append(retweets[i].id)
            print(retweets[i].id)
        return pd.DataFrame([id_tweet, sentiment, retweet_list, timestamp, faves, tweet_text])
    except tweepy.TweepError:
        print('Tweet unavailable.')



def buildGraph(id_tweet):

    df = getRetweets(id_tweet)

    # create graph

    for tweet in df:
        temp = getRetweets(tweet)
        # add to graph

