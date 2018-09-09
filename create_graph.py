import networkx as nx
import os
import pandas as pd
# from gather_tweets import clean_tweet
import matplotlib.pyplot as plt
import ast


def clean_tweet(tweet):
    a = 0
    for i in range(0, 6):
        try:
            tweet[0][i] = ast.literal_eval(tweet[0][i])
        except:
            a += 1
    return tweet


files = os.listdir('data/retweets_followers')
stats = []
j = 0
G = nx.Graph()

users = set()

for file in files:
    print('data/retweets_followers/' + str(file))
    print('Saved tweet number:', j)
    j += 1
    tweet = pd.read_csv('data/retweets_followers/' + str(file), usecols=[1])
    # tweet.columns = [0]
    tweet = clean_tweet(tweet)
    users.update(tweet.iloc[8])


for file in files:
    print('data/retweets_followers/' + str(file))
    print('Saved tweet number:', j)
    j += 1
    tweet = pd.read_csv('data/retweets_followers/' + str(file), usecols=[1])
    # tweet.columns = [0]
    tweet = clean_tweet(tweet)

    followers = ast.literal_eval(tweet.iloc[7].tolist()[0])
    for f in followers:
        if str(f) in users:
            G.add_edge(ast.literal_eval(tweet.iloc[0][0]), f)


nx.write_edgelist(G, 'graph.csv', delimiter=',')
d = nx.degree(G)
nx.draw(G, nodelist=d.keys(), node_size=[v for v in d.values()])
plt.show()



