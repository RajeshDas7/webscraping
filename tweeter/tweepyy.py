import tweepy
import csv
data=open('az21.txt','w',encoding='utf-8')

consumer_key = "nvEV4sEBSWM3HjwkcPu9ug6VR" 
consumer_secret = "3I6VFDNLbRGGkq7um1RqouLFs7EArViu3KoKMdN72QzN2i7Mwm"
access_key = "1086269917295390720-fc1DqWryLNZIIibNiHsJ0yVdAqJiYn"
access_secret = "ITWTam10QS07n5dQ4JNNpIfJedAiHtrhiRY2xw0k0gZsh"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
auth.set_access_token(access_key, access_secret) 

api = tweepy.API(auth)
with open('wiki_name.csv','r',encoding='UTF-8') as inp, open('tweeter_screen_names.csv','w') as out:
    writer=csv.writer(out)
    
    for row in csv.reader(inp):
        # print(row[0])
        if row:
            try:
                user =api.search_users(row[0])
                temp=[]
                flag=1
                for i in user:
                    if i.verified== True:
                        temp.append(i.screen_name)
                        flag=0
                if flag:
                    print(row[0],"not_varified")        
                print(temp)
            except Exception as e:
                print(e)
    







# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


# data.write(str(user))
# print(str(user))

    
    # print(i.screen_name)
    
        # print(i.screen_name)









# user = api.get_user('narendramodi')
# was=str(user)
# # print(user)
# data.write(was)
# # data.close
# print('done')
# # print(user.screen_name)
# # print(user.followers_count)
# # for friend in user.friends():
# #    print(friend.screen_name)