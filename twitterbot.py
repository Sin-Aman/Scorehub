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
import flag
import schedule
import time
from datetime import datetime

# goal is to print the following:
# [team_a or team_b] just scored at minute [time]!
# [team_emoji][team_a]      [score_a]
# Vs
# [team_emoji][team_b]      [score_b]

# Loads the .env file for the credentials
load_dotenv()
trackscore_1 = []
trackscore_1.append(0)
trackscore_2 = []
trackscore_2.append(0)
scorehaschanged = False

def job():
  start_time = 11
  end_time = 13
  current_time = datetime.now().hour
  if current_time < start_time:
    print("The match has not started, it will start at 11am")
    print(current_time)
  elif current_time >= end_time:
    print('The game is over, tomorrow there will be more games')
    print(current_time)
  else:
    params = {
      "api_key": os.environ.get('serp_api_key'),
      "device": "desktop",
      "engine": "google",
      "q": "world cup",
      "location": "United states",
      "google_domain": "google.com",
      "gl": "us",
      "hl": "en",
      "no_cache": "true"
    }

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
        teamthatscores = []
        status = hh.get('status', "not yet played")
        time = hh.get('time', "LIVE NOW")

    # we need to write escape statment
        for ss in teams:
            x = ss.get('score', "no score")
            scores.append(x)

        if scores[0] > scores[1]:
           teamthatscores = team1
        else:
           teamthatscores = team2

        scorehaschanged = False
        if scores[0] != trackscore_1[0]:
          trackscore_1.clear()
          trackscore_1.append(scores[0])
          scorehaschanged = True

        if scores[1] != trackscore_2[0]:
          trackscore_2.clear()
          trackscore_2.append(scores[1])
          scorehaschanged = True

        if status == "FT":
          print('Game is over')
          break
        else:
          if scorehaschanged:
            #If the scores have not changes or they are both 0 then do not print
            print(team1  +"      "+ scores[0] )
            print("Vs")
            print(team2 + "      "+ scores[1] )
            print(" ")
            # Status: Live Now, "Half-time", "FT", 
            # "date":"Today",
            # status = hh.get('status', "not yet played")
            #time = hh.get('time', "LIVE NOW")
            print("status:" +"       " +status )
            print("Time:" +" " + time)
            print("===============================")
            api.update_status("FIFA WORLD CUP QATAR⚽⚽\n" + teamthatscores + " scored💥\n" + team1  +"      "+ scores[0] +"\n Vs \n" + team2 +" "+ scores[1] +"\n")
            print("tweeted")
          else:
            print("Score has not changed at minute: " + status[4:])
        trackscore_1.append(scores[0])
        trackscore_2.append(scores[1])
        break
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
