from time import sleep
import os

import tweepy

from settings import INTERVAL
from helper import random_image, random_gif, random_function
from secret import *

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_KEY =  os.environ['TWITTER_ACCESS_KEY']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def post_media():
    """ Post a random image or random gif. """
    media = random_function()()
    if media is None:
        return False
    media_ids = [api.media_upload(media).media_id_string]
    api.update_status(media_ids=media_ids)
    return True


def _delete_tweets(count=20):
    """ Delete `count` tweets. If not specified, count is 20 by default. """
    tweets = api.user_timeline(count=count)
    for t in tweets: 
        api.destroy_status(t.id)


def post_tweets():
    """ Post images or gifs at an interval of `INTERVAL` seconds  """
    while True:
        post_media()
        sleep(60)


if __name__ == '__main__':
    post_tweets()