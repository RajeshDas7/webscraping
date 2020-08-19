import tweepy

consumer_key = "nvEV4sEBSWM3HjwkcPu9ug6VR"
consumer_secret = "3I6VFDNLbRGGkq7um1RqouLFs7EArViu3KoKMdN72QzN2i7Mwm"
access_token = "1086269917295390720-rwbnIFrN2tjmQNjmr4dh849WH2Aewk"
access_token_secret = "hwweAzNe6ltT9MaFHRaFTk7ZJPd04a6HdFHuDUDEKniyH"

import csv
# import pandas as pd

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('caa.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

# query = 'python'
# max_tweets = 1000
# searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
# print(searched_tweets)

for tweet in tweepy.Cursor(api.search,q="#caa",count=100,lang="en",since="2017-04-03").items():
    # print(tweet)
    # print (tweet.created_at, tweet.text)
    csvWriter.writerow(
        [tweet.created_at, tweet.favorite_count, tweet.text.encode('utf-8')])
