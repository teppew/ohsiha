from django.shortcuts import render
import tweepy  # https://github.com/tweepy/tweepy
import csv
import sys
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
import plotly.offline as pyo
#import plotly.graph_objs as go
#import plotly.express as px
import numpy as np
import pandas as pd
import pandas_highcharts.core

def twitter_streamer(hashtag, count):
    # Twitter API credentials
    consumer_key = "ITGUMYGW0RcKVmNx1zBHgg8vE"
    consumer_secret = "E3ybqc5t8g8Xxn6UdxDTs29qZsBB3v8hHh1m6jRTI7Dtvjo7B8"
    access_key = "1114139053019025409-OsHVYXqIWaxrr6EWXcvbt9WylbR0AE"
    access_secret = "wrpbI6uufwOrOl6FOo84XYPU6pIz4Jyehb4oByhRA92a0"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    query = hashtag
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, exclude='retweets', lang="en", tweet_mode='extended').items(count)]
    alltweet_list = {}
    i=1
    for tweet in searched_tweets:
        username = tweet.user.screen_name
        created = tweet.created_at
        text = tweet.full_text.replace("\n", "")
        location = tweet.user.location
        alltweet_list[i] = [location, username , created, text]
        i+=1

    # Sentiment analysis
    positive = 0
    negative = 0
    neutral = 0

    for tweet in alltweet_list:
        polarity = 0
        text = TextBlob(alltweet_list[tweet][3])
        polarity = text.sentiment.polarity
        if polarity < 0:
            negative += 1
        elif polarity == 0:
            neutral += 1
        elif polarity > 0:
            positive += 1

    polaritys = [positive, negative, neutral, hashtag, count]
    return polaritys, alltweet_list

