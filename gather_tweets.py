import os
import numpy as np
from get_retweets import getRetweets
import pandas as pd
import ast
import networkx as nx


def gatherTweets():

    j = 0
    data = pd.read_csv('data/data_all.csv')

    for index, row in data.iloc[4437:, :].iterrows():
        print('Number: ', j+4437)
        j += 1
        getRetweets(int(row['Tweet ID']), row['Sentiment'], row['Tweet'])


def clean_tweet(tweet):
    a = 0
    for i in range(0, 6):
        try:
            tweet[0][i] = ast.literal_eval(tweet[0][i])
        except:
            a += 1
    return tweet


def getSteps(id_tweet, num_steps):
    files = os.listdir('data/retweets')
    if str(id_tweet) + '.csv' not in files:
        tweet = getRetweets(id_tweet)
    else:
        tweet = pd.read_csv('data/retweets/' + str(id_tweet) + '.csv', usecols='0')
        tweet.columns = [0]
        tweet = clean_tweet(tweet)
    if tweet is None:
        return num_steps
    steps = np.zeros(len(tweet[0][2]))
    j = 0
    for i in tweet[0][2]:
        steps[j] = getSteps(i, num_steps + 1)
        j += 1
    if len(steps) == 0:
        return num_steps
    return np.max(steps)


def get_stats():
    files = os.listdir('data/retweets')
    stats = []
    j = 0

    for file in files:
        print('data/retweets/' + str(file))
        print('Saved tweet number:', j)
        j += 1
        tweet = pd.read_csv('data/retweets/' + str(file), usecols='0')
        tweet.columns = [0]
        tweet = clean_tweet(tweet)

        num_retweets = len(tweet[0][2])
        num_faves = tweet[0][4]
        num_retweets_norm = len(tweet[0][2])
        num_faves_norm = float(tweet[0][4])
        followers = float(tweet[0][6])

        if followers != 0:
            num_retweets_norm = len(tweet[0][2]) / followers
            num_faves_norm = float(tweet[0][4]) / followers

        stats.append([num_retweets, num_retweets_norm, num_faves, num_faves_norm, getSteps(tweet[0][0], 0), followers, tweet[0][1]])

    print(stats)
    sent = 6

    positive_stats = [x for x in stats if x[sent] == 'POSITIVE']
    negative_stats = [x for x in stats if x[sent] == 'NEGATIVE']
    neither_stats = [x for x in stats if x[sent] == 'NEITHER']

    ps = pd.DataFrame(positive_stats)
    ns = pd.DataFrame(negative_stats)
    nes = pd.DataFrame(neither_stats)

    ps.to_csv('data/positive.csv')
    ns.to_csv('data/negative.csv')
    nes.to_csv('data/neither.csv')

gatherTweets()
# get_stats()

