import tweepy

consumer_key = "nvEV4sEBSWM3HjwkcPu9ug6VR" 
consumer_secret = "3I6VFDNLbRGGkq7um1RqouLFs7EArViu3KoKMdN72QzN2i7Mwm"
access_key = "1086269917295390720-8FXXo4xdsUib4kRX2nKLOwesgfBla5"
access_secret = "a7CKfLfqHLrplJaZJXjAuL9yQi4AOrwJqZDpNNxOHKGce"
username='Narendra_Modi'
def get_tweets(username):   
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 

        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(len(tmp))
get_tweets(username) 
# Driver code 
# if __name__ == '__main__': 
  
#     # Here goes the twitter handle for the user 
#     # whose tweets are to be extracted. 
#     get_tweets("twitter-handle")  