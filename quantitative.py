import numpy as np
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt


def calculate_stats():
    positive_stats = ps = pd.read_csv('data/positive.csv').drop(['Unnamed: 0'], axis=1)
    negative_stats = ns = pd.read_csv('data/negative.csv').drop(['Unnamed: 0'], axis=1)
    neither_stats = nes = pd.read_csv('data/neither.csv').drop(['Unnamed: 0'], axis=1)

    print()
    names = ['num_retweets', 'num_retweets_norm', 'num_faves', 'num_faves_norm', 'steps', 'followers', 'sentiment']
    # print('-------------------------Mean:-------------------------')
    # for i in range(0, 6):
    #     print('###', names[i], '###')
    #     print('Positive:', np.mean((np.array(positive_stats)[:, i]).astype(np.float)))
    #     print('Negative:', np.mean((np.array(negative_stats)[:, i]).astype(np.float)))
    #     print('Neutral', np.mean((np.array(neither_stats)[:, i]).astype(np.float)))
    #
    # print('-------------------------Total:-------------------------')
    # for i in range(0, 6):
    #     print('###', names[i], '###')
    #     print('Positive:', np.sum((np.array(positive_stats)[:, i]).astype(np.float)))
    #     print('Negative:', np.sum((np.array(negative_stats)[:, i]).astype(np.float)))
    #     print('Neutral', np.sum((np.array(neither_stats)[:, i]).astype(np.float)))

    # print('-------------------------Variance:-------------------------')
    # for i in range(0, 6):
    #     print('###', names[i], '###')
    #     print('Positive:', np.var((np.array(positive_stats)[:, i]).astype(np.float)))
    #     print('Negative:', np.var((np.array(negative_stats)[:, i]).astype(np.float)))
    #     print('Neutral', np.var((np.array(neither_stats)[:, i]).astype(np.float)))


    print('-------------------------T - test:-------------------------')
    for i in range(0, 6):
        print('###', names[i], '###')

        m1 = np.mean((np.array(positive_stats)[:, i]).astype(np.float))
        std1 = np.std((np.array(positive_stats)[:, i]).astype(np.float))
        num1 = len(np.array(positive_stats))

        m2 = np.mean((np.array(negative_stats)[:, i]).astype(np.float))
        std2 = np.std((np.array(negative_stats)[:, i]).astype(np.float))
        num2 = len(np.array(negative_stats))

        m3 = np.mean((np.array(neither_stats)[:, i]).astype(np.float))
        std3 = np.std((np.array(neither_stats)[:, i]).astype(np.float))
        num3 = len(np.array(neither_stats))

        print('1', ss.ttest_ind_from_stats(m1, std1, num1, m2, std2, num2))
        print('2', ss.ttest_ind_from_stats(m1, std1, num1, m3, std3, num3))
        print('3', ss.ttest_ind_from_stats(m2, std2, num2, m3, std3, num3))


calculate_stats()
