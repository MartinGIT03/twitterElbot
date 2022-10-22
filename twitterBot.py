
import tweepy

def bot(message):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler() # Insert api keys here  
    auth.set_access_token() 

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(message)

