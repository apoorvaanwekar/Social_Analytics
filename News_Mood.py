
# Dependencies
import tweepy
# import json
import numpy as np
#import apikeys
# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# Twitter API Keys
consumer_key = "sY8fauoEtegrERuNmKGtMAz54"
consumer_secret = "h1g3mTdGGPJNFFPoEbcvGJvkwUbItHUwv8J0Md06Xk216N0SVD"
access_token = "3168989036-8Uabrs2l1Edzv1vMynmt9AVsNId74qjHnjJ2nDA"
access_token_secret = "efgg82mNboqI57xeg2eXo6W60tzubYIv5GN6u2WNt75js"
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# Target User Account
target_user = ('@BBC', '@CBSNews', '@CNN', '@FoxNews', '@nytimes')
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
for page in range(10):
        public_tweets = api.user_timeline(target_user, page=page)
        for tweet in public_tweets:
            text = tweet['text']
            scores = analyzer.polarity_scores(text)
            compound = scores['compound']
            pos = scores['pos']
            neu = scores['neu']
            neg = scores['neg']
            compound_list.append(compound)
            positive_list.append(pos)
            negative_list.append(neg)
            neutral_list.append(neu)

print('')
print(target_user)
print(f'Compound Score: {compound}')
print(f'Positive Score: {pos}')
print(f'Neutral Score: {neu}')
print(f'Negative Score: {neg}')