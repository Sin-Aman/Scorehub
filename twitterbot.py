# Necessary packages
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
from bs4 import BeautifulSoup # webscrapping
import json # Extract the json
import webbrowser
import os
# This is for twitter api
import tweepy
from dotenv import load_dotenv
from serpapi import GoogleSearch

# goal is to print the following:
# [team_a] just scored against [team_b]: [score_a] - [score_b] at minute [time]

params = {
  "api_key": "7835e3432f047519f65477d6e2afce616ca02bf13761993d9159ba6cd9d56cdf",
  "device": "desktop",
  "engine": "google",
  "q": "world cup",
  "location": "United states",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "no_cache": "true"
}

# Loads the .env file for the credentials
load_dotenv()

# Credentials set in the .env file
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

search = GoogleSearch(params)
results = search.get_dict()
res = results['sports_results']['games']

for hh in res:
    teams = hh['teams']
    team1 = teams[0]['name']
    team2 = teams[1]['name']
    scores = []

    for ss in teams:
        x = ss.get('score', "no score")
        scores.append(x)

    print(team1  +"      "+ scores[0]   )
    print("Vs")
    print(team2 + "      "+ scores[1] )
    print(" ")
    status = hh.get('status', "not yet played")
    time = hh.get('time', "LIVE NOW")
    print("status:" +"       " +status )
    print("Time:" +" " + time)
    print("===============================")

    api.update_status("FIFA WORLD CUP QATAR⚽⚽\n" + team1  +"      "+ scores[0] +"\n Vs \n" + team2 +" "+ scores[1] +"\n" + "\nstatus:" +"       " +status +"\n" + "Time:" +" " + time)
    print("tweeted")
    break
