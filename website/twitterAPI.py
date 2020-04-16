from django.shortcuts import render
import tweepy  # https://github.com/tweepy/tweepy
import csv
import sys
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
import plotly.offline as pyo
import numpy as np
import pandas as pd
import pandas_highcharts.core
from website import locations
import os
import preprocessor as p
from website import cleaner

def twitter_streamer(hashtag, count):
    # Twitter API credentials
    auth = tweepy.OAuthHandler(os.environ.get('consumer_key'), os.environ.get('consumer_secret'))
    auth.set_access_token(os.environ.get('access_key'), os.environ.get('access_secret'))
    api = tweepy.API(auth)

    # If user enter many word, this separetas them and assumes that the first word is the wanted one.
    hashtag = hashtag.split(" ")
    try:
        hashtag.remove("")
    except:
        pass
    hashtag = hashtag[0]

    if hashtag[0] == "#":
        query = hashtag
    else:
        query = "#" + hashtag

    searched_tweets = [status for status in
                       tweepy.Cursor(api.search, q=query, exclude='retweets', tweet_mode='extended').items(
                           count)]

    # Dict of lists with information about [text, created at]
    alltweet_list = {}
    tweet_coordinates = []
    i = 1
    for tweet in searched_tweets:
        username = tweet.user.screen_name
        created = tweet.created_at
        text = tweet.full_text.replace("\n", "")
        location = tweet.user.location

        if locations.location_verifier(location):
            location = locations.location_search(location)
            tweet_coordinates.append(location)
        alltweet_list[i] = [text, created]
        i += 1


    # Sentiment analysis
    positive = 0
    negative = 0
    neutral = 0
    subjective = 0
    objective = 0


    for tweet in alltweet_list:
        cleanded_tweet = cleaner.cleaner_function(alltweet_list[tweet][0])
        text = TextBlob(cleanded_tweet)
        polarity = text.sentiment.polarity
        subjectivity = text.sentiment.subjectivity

        # Checking polarity
        if polarity < 0:
            negative += 1
        elif polarity == 0:
            neutral += 1
        else:
            positive += 1

        # Checking subjectivity
        if subjectivity > 0.5:
            subjective += 1
        else:
            objective += 1

    sentiments = [positive, negative, neutral, objective, subjective, i-1, query]


    return sentiments, tweet_coordinates

