import os

import tweepy
from dotenv import load_dotenv

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

# Checks if the credentials entered are correct
def authenticate():
    if not api.verify_credentials():
        print('Authentication: FAILED')
        return False
    else:
        print('Authentication: OK')
        return True

def tweet():
    # If authenticate returns true, execute the following
    if authenticate():
        # Calls the API to tweet the following
        api.update_status('Hello ScoreHub!')
        print('Tweet has been sent!')
    # If authenticate returns false, print the following
    else:
        print('Tweet has not been sent.')

if __name__ == "__main__":
    tweet()