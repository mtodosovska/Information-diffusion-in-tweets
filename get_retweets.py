import tweepy
import pandas as pd
import time

consumer_token = 'H7hrtScuUkntKTO7oMQUJpCru'
consumer_secret = 'Zqy8jfZU9KMug81cyXIm27BsbN8NsT4hNa5jiTgbyo2XW5l6gR'
access_token = '1485883142-vWEIFUsvp0iGu7pbln3WJWj0IwSFyBdOolUN1Zi'
access_token_secret = 'BQJoTSnWTUzr8QXmgGdtvuEK4VleO1pCklpEkMmJsxwXU'


def getRetweets(id_tweet, sentiment='', tweet_text=''):

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print('Getting tweet from api. Id = ', id_tweet)

    try:
        retweets = []
        print('wainting...')
        tweet = api.get_status(id_tweet, monitor_rate_limit=True, wait_on_rate_limit=True)
        if tweet.retweet_count > 0:
            retweets = api.retweets(id_tweet, monitor_rate_limit=True, wait_on_rate_limit=True)
        faves = tweet.favorite_count
        timestamp = tweet.created_at
        followers = tweet.author.followers_count
        print('Followers:', followers)
        if followers <= 50000:
            return None
        else:
            id_user = tweet.author.id
            retweet_list = []
            for i in range(0, len(retweets)):
                retweet_list.append(retweets[i].id)
            followers_list = []
            pages = 0
            print('Approximatelly', followers/4500, 'pages.')
            for page in tweepy.Cursor(api.followers_ids, id=tweet.author.id).pages():
                followers_list.extend(page)
                time.sleep(60)
                pages += 1
                print('Page:', pages)

        if tweet is not None:
            tw = pd.DataFrame([id_tweet, sentiment, retweet_list, timestamp, faves, tweet_text, followers, followers_list, id_user])
            tw.to_csv('data/retweets_followers/' + str(id_tweet) + '.csv')
        return pd.DataFrame([id_tweet, sentiment, retweet_list, timestamp, faves, tweet_text, followers, followers_list, id_user])
    except tweepy.TweepError as e:
        print('Tweet unavailable.')
        print(e.reason)
