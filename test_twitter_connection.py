def test_twitter_connection():
    # Import the tweepy library
    import tweepy

    # Set up the API credentials
    consumer_key='TzOJVDCMPjBiBW8HA1oSFEtnS'
    consumer_secret='OD83yNUR4gSFPR48ssNkcofevgCIOv67lxwYBBMo8hfak6P1EZ'
    access_token='1593790468940132352-M1UKRHmfdu6YkD3y7FbGvjMzV9vrf9'
    access_token_secret='eMNKhKbyfxmEygopJ3hxFF5CynsCadk6tFkoXAfoaPB6u'
    serp_api_key='205beafd651f0a0a67521529a1957c0ce2bfa62fc17a89695411d7541dcc6099'

    # Authenticate using the API credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create an API object
    api = tweepy.API(auth)

    # Verify that the connection is successful
    assert api.verify_credentials()