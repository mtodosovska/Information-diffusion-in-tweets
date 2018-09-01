import os
import pandas as pd
import time
import datetime

#Presmetuva po kolku vreme od objavuvanjeto na tvitot bil ispraten privot retweet
def calculate_first_retweet( category ):
    files = os.listdir(os.path.join('data',category))
    path=(os.path.join('data',category))
    min=9999999999999
    for file in files:
        tweet=pd.read_csv(os.path.join(path,file))
        retvitovi=tweet.ix[2,1]
        retvitovi=retvitovi.replace('[','')
        retvitovi=retvitovi.replace(']','')
        if (len(retvitovi)>3):
            retweets = retvitovi.split(',')
            first=retweets[0]
            path_file=os.path.join('data','retweets')
            retweet_file=pd.read_csv(os.path.join(path_file,str(first)+'.csv'))
            retweet_time=retweet_file.ix[3,1]

            f = "%Y-%m-%d %H:%M:%S"

            date1=time.strptime(retweet_time,f)
            time_tweet = tweet.ix[3, 1]
            # time_tweet ="2015-07-11 13:49:57"
            # a="2015-07-11 16:49:57"
            # b="%Y-%m-%d %H:%M:%S"
            # date1=time.strptime(a,b)
            # print(time_tweet)

            date = time.strptime(time_tweet, f)
            # print(date)
            #  print(time.mktime(date1)-time.mktime(date)) # ova vraka sekundi
            sec=time.mktime(date1) - time.mktime(date)
            if sec<min:
                min=sec
     #       print(str(datetime.timedelta(seconds=sec))) # razlika vo sekundi od objavuvanjeto na tvitot i prviot retvit
    print("Shortest time to post first retweet is " + str(datetime.timedelta(seconds=min)))


# Presmetuva za X casovi kolku retvitovi ima
def calculate_retweets_afterX( category , hours ):
    files = os.listdir(os.path.join('data',category))
    path=(os.path.join('data',category))
    total_retweets=0;
    max=0;
    for file in files:
        tweet=pd.read_csv(os.path.join(path,file))
        retvitovi=tweet.ix[2,1]
        retvitovi=retvitovi.replace('[','')
        retvitovi=retvitovi.replace(']','')

        if (len(retvitovi)>3):
            retweets = retvitovi.split(',')
            for retweet in retweets:
                first = retweet.strip()
                path_file = os.path.join('data','retweets')
                retweet_file = pd.read_csv(os.path.join(path_file, str(first) + '.csv'))
                retweet_time = retweet_file.ix[3, 1]

                f = "%Y-%m-%d %H:%M:%S"

                date1 = time.strptime(retweet_time, f)
                time_tweet = tweet.ix[3, 1]
                date = time.strptime(time_tweet, f)
                sec = time.mktime(date1) - time.mktime(date)
               # print(sec)
                h = sec / 3600
                if h< hours:
                    total_retweets=total_retweets+1

        if max< total_retweets:
            max=total_retweets

        #print(total_retweets)
        total_retweets=0;
    print("Max retweets within %d hours is %d"%(hours,max))



print("Positive tweets: ")
calculate_first_retweet('positive')
calculate_retweets_afterX("positive", 1)

print("Negative tweets: " )
calculate_first_retweet('negative')
calculate_retweets_afterX("negative", 1)

print("Neither tweets: ")
calculate_first_retweet('neither')
calculate_retweets_afterX("neither", 1)

