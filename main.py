import quotes
import tweepy 
import datetime 
import time
import random
import refresh

refresh.refresh()
consumer_key = 'TGB9bGx2sUTXOZE5aeWmfBe83' 
consumer_secret = 'oQ5qY568VOttOWJJip1saIWws9zsz9dpNcQbIikS1dud0u12pE' 
access_token = '1271549237709463552-pcIA9gWGzlRTWcPNpuTL5zB3C4azqW' 
access_token_secret = 'kqJYwEAvsXJg4PZq8cmKCkdjlyvVAlTp7wLz2p39iIify' 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet():
    quote = quotes.generate_chain(0,1)
    api.update_status(quote)
    print("I tweeted: " + quote)

for _ in range(47):
    tweet()
    time.sleep(1800)
