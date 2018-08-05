import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_stats():
    positive_stats = ps = pd.read_csv('data/positive.csv').drop(['Unnamed: 0'], axis=1)
    negative_stats = ns = pd.read_csv('data/negative.csv').drop(['Unnamed: 0'], axis=1)
    neither_stats = nes = pd.read_csv('data/neither.csv').drop(['Unnamed: 0'], axis=1)

    print()
    names = ['num_retweets', 'num_retweets_norm', 'num_faves', 'num_faves_norm', 'steps', 'followers', 'sentiment']
    print('-------------------------Mean:-------------------------')
    for i in range(0, 6):
        print('###', names[i], '###')
        print('Positive:', np.mean((np.array(positive_stats)[:, i]).astype(np.float)))
        print('Negative:', np.mean((np.array(negative_stats)[:, i]).astype(np.float)))
        print('Neutral', np.mean((np.array(neither_stats)[:, i]).astype(np.float)))

    print('-------------------------Total:-------------------------')
    for i in range(0, 6):
        print('###', names[i], '###')
        print('Positive:', np.sum((np.array(positive_stats)[:, i]).astype(np.float)))
        print('Negative:', np.sum((np.array(negative_stats)[:, i]).astype(np.float)))
        print('Neutral', np.sum((np.array(neither_stats)[:, i]).astype(np.float)))


calculate_stats()
