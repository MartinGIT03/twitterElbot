import tweepy
from config import * 

def bot(message):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(APItweepy_OAuthHandler[0], APItweepy_OAuthHandler[1])
    auth.set_access_token(APIset_access_token[0], APIset_access_token[1])

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(message)
