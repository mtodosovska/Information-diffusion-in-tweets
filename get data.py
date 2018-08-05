import pandas as pd
import math
import numpy as np

data1 = pd.read_csv('data\ElectoralTweetsData\AnnotatedTweets_1.txt', delimiter='\t', usecols=['createdat', 'id', 'sentiment', 'tweet'])
data2 = pd.read_csv('data\ElectoralTweetsData\AnnotatedTweets_2.txt', delimiter='\t', usecols=['createdat', 'id', 'sentiment', 'tweet'])
data_e = data1.append(data2)

cr = list(data_e['createdat'])
id = list(data_e['id'])
sentiment = list(data_e['sentiment'])

tweet = list(data_e['tweet'])
names = ['Tweet ID', 'Sentiment', 'Tweet']
data_electoral = pd.DataFrame(columns=names)
cr_id = [str(x).split() for x in cr]

i = 0
for x, y in zip(cr_id, id):
    if x[0] != 'BLANK' and not math.isnan(float(y)):
        l = pd.DataFrame(np.zeros(3))
        data_electoral = data_electoral.append(l)
        data_electoral.iat[i, 0] = str(x[1]) + str(y)

        if sentiment[i] == 'negative emotion':
            data_electoral.iat[i, 1] = 'NEGATIVE'
        elif sentiment[i] == 'positive emotion':
            data_electoral.iat[i, 1] = 'POSITIVE'
        elif sentiment[i] == 'neither positive nor negative':
            data_electoral.iat[i, 1] = 'NEITHER'
        else:
            data_electoral.iat[i, 1] = sentiment[i]

        data_electoral.iat[i, 2] = tweet[i]
        i += 1


# data_stance = pd.DataFrame(columns=names)
datas_11 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-all-annotations.txt', delimiter='\t', usecols=['ID', 'Tweet', 'Sentiment'])
datas_12 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-ids.txt', delimiter='\t')
datas_1 = datas_11.merge(datas_12, on='ID')

datas_21 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-all-annotations.txt', delimiter='\t', usecols=['ID', 'Tweet', 'Sentiment'])
datas_22 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-ids.txt', delimiter='\t')
datas_2 = datas_11.merge(datas_12, on='ID')

datas_31 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-all-annotations.txt', delimiter='\t', usecols=['ID', 'Tweet', 'Sentiment'])
datas_32 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-ids.txt', delimiter='\t')
datas_3 = datas_11.merge(datas_12, on='ID')

datas_41 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-all-annotations.txt', delimiter='\t', usecols=['ID', 'Tweet', 'Sentiment'])
datas_42 = pd.read_csv('data\stance-data-all-annotations\data-all-annotations\\testdata-taskA-ids.txt', delimiter='\t')
datas_4 = datas_11.merge(datas_12, on='ID')

datas_1 = datas_1.append(datas_2)
datas_3 = datas_3.append(datas_4)
datas_1 = datas_1.append(datas_3)
datas_1 = datas_1.drop(labels='ID', axis='columns')

data = data_stance = datas_1[names]
# data = data_electoral.append(data_stance)
data.to_csv('data/data_all.csv')



