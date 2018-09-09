import networkx as nx
import os
import pandas as pd
# from gather_tweets import getSteps
# from gather_tweets import clean_tweet
import matplotlib.pyplot as plt
import ast
import numpy as np
from get_retweets import getRetweets
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model


def gatherTweets():

    j = 0
    data = pd.read_csv('data/data_all.csv')

    for index, row in data.iloc[168:, :].iterrows():
        print('Number: ', j)
        j += 1
        tweet = getRetweets(int(row['Tweet ID']), row['Sentiment'], row['Tweet'])


def clean_tweet(tweet):
    a = 0
    for i in range(0, 6):
        try:
            tweet.iloc[i][0] = ast.literal_eval(tweet.iloc[i][0])
        except:
            a += 1
    return tweet


def getSteps(id_tweet, num_steps):
    files = os.listdir('data/retweets')
    if str(id_tweet) + '.csv' not in files:
        tweet = getRetweets(id_tweet)
    else:
        tweet = pd.read_csv('data/retweets/' + str(id_tweet) + '.csv', usecols=[1])
        tweet.columns = [0]
        tweet = clean_tweet(tweet)
    if tweet is None:
        return num_steps
    steps = np.zeros(len(tweet[0][2]))
    if len(steps) >= 10:
        print('Hooray!')
        print('Hooray!')
    j = 0
    for i in tweet[0][2]:
        steps[j] = getSteps(i, num_steps + 1)
        j += 1
    if len(steps) == 0:
        return num_steps
    return np.max(steps)


def get_data():
    files = os.listdir('data/retweets')
    j = 0
    data = pd.DataFrame()

    for file in files:

        print('data/retweets/' + str(file))
        print('Saved tweet number:', j)
        tweet = pd.read_csv('data/retweets/' + str(file), usecols=[1], encoding='latin1')
        # tweet.columns = [0]

        tweet = clean_tweet(tweet)
        id_tweet = int(tweet.iloc[0][0])
        num_retweets = len(tweet.iloc[2][0])
        num_faves = int(tweet.iloc[4][0])
        followers = float(tweet.iloc[6][0])
        retweets = tweet.iloc[2][0]
        steps = getSteps(tweet.iloc[0][0], 0)
        retweeters = []
        if len(retweets) > 0:
            for id in retweets:
                if str(id) + '.csv' in files:
                    rt = pd.read_csv('data/retweets/' + str(id) + '.csv', usecols=[1], encoding='latin1')
                    if rt is not None:
                        retweeters.append(float(rt.iloc[6][0]))
                    else:
                        retweeters.append(0)
                else:
                    retweeters.append(0)
        else:
            retweeters.append(0)

        row = [np.mean(retweeters), num_retweets, num_faves, followers, steps]

        data = data.append(pd.DataFrame(row).transpose())

    data.to_csv('data/features_labels.csv')
    return data
data = pd.read_csv('data/features_labels.csv', encoding='latin1').drop('Unnamed: 0', axis=1).drop(325)
# data = get_data()
features = data.iloc[:, 0:4]
labels = data.iloc[:, 4].tolist()

train, test, labels_train, labels_test = train_test_split(
    features, labels,
    test_size=0.20, random_state=42)

b_rf = RandomForestClassifier(n_estimators=1000, n_jobs=-1, verbose=0, class_weight='balanced', bootstrap=True)
print('Fitting..')
b_rf.fit(train, labels_train)
results = b_rf.predict(test)
print('score:', accuracy_score(labels_test, results))
#
print('Linear Regression')
regr = linear_model.LinearRegression()
regr.fit(train, labels_train)
pred = regr.predict(test)
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(labels_test, pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(labels_test, pred))


# Plot outputs
plt.scatter(test.iloc[:, 1].tolist(), labels_test,  color='black')
plt.plot(test, pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
