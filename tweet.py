import os
import twitter
from ayahat import Ayah

API_KEY = os.environ.get('api_key')
API_SECRET = os.environ.get('api_secret')
ACCESS_TOKEN = os.environ.get('access_token')
ACCESS_SECRET_TOKEN = os.environ.get('access_secret_token')
#BEARER_TOKEN = os.environ.get('b_token')


class TweetQ:
    def __init__(self):
        self.twitter_api = self.get_api()


    def get_api(self):
        api = twitter.Api(consumer_key=API_KEY, 
        consumer_secret=API_SECRET,
        access_token_key=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET_TOKEN)

        return api

    def tweet(self, message):
        """Send a Tweet"""
        self.twitter_api.PostUpdate(message)



