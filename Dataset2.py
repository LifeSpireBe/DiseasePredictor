import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = "EgjCgVxayfmnj68PXiVKu1PVj"
consumer_secret = "QFszM57LLN4GyIOmPBG9Q1bjWceDj7yGBIEuF2xWCyt93BbZ8Z"
access_token = "1199917326285426690-MWVeRP6oBVW7b6X5FEHJhwpNBB2bXf"
access_token_secret = "BqqWCmW1hUGlZhLLyXyjeFYVByDoJlPGIYwpGU949Y89x"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2019-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search,q="#timemachine",count=100,
                           lang="en",
                           since="2019-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search,q="#cute",count=100,
                           lang="en",
                           since="2019-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search,q="#stockmarket",count=100,
                           lang="en",
                           since="2019-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search,q="#panda",count=100,
                           lang="en",
                           since="2019-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])