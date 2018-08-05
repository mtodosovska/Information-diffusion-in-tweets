import tweepy
import pandas as pd

consumer_token = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


def getRetweets(id_tweet, sentiment='', tweet_text=''):

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print('Getting tweet from api. Id = ', id_tweet)

    try:
        retweets = []
        tweet = api.get_status(id_tweet, wait_on_rate_limit=True)
        if tweet.retweet_count > 0:
            retweets = api.retweets(id_tweet, wait_on_rate_limit=True)
        faves = tweet.favorite_count
        timestamp = tweet.created_at
        followers = tweet.author.followers_count
        retweet_list = []
        for i in range(0, len(retweets)):
            retweet_list.append(retweets[i].id)
        if tweet is not None:
            tw = pd.DataFrame([id_tweet, sentiment, retweet_list, timestamp, faves, tweet_text, followers])
            tw.to_csv('data/retweets/' + str(id_tweet) + '.csv')
        return pd.DataFrame([id_tweet, sentiment, retweet_list, timestamp, faves, tweet_text, followers])
    except tweepy.TweepError as e:
        print('Tweet unavailable.')
        print(e.reason)
