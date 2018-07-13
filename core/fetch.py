import tweepy
import os
import inspect
import datetime


def fetch_tweets(consumer_key='', consumer_secret='', access_token_key='', access_token_secret=''):
    os.makedirs('build/cache', exist_ok=True)
    if any(not i for i in [consumer_key, consumer_secret, access_token_key, access_token_secret]):
        secrets = _load_local_secret()
        consumer_key = secrets['consumer_key']
        consumer_secret = secrets['consumer_secret']
        access_token_key = secrets['access_token_key']
        access_token_secret = secrets['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(key=access_token_key, secret=access_token_secret)
    api = tweepy.API(auth)

    original_tweets = api.user_timeline(screen_name='realDonaldTrump',
                                        count=200,
                                        tweet_mode="extended")
    return _parse_tweets(original_tweets)


def _load_local_secret():
    fp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../.secret'
    result = {}
    with open(fp, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            key, value = line.split('=')
            result[key] = value
    return result


def _parse_tweets(original_tweets):
    since = datetime.datetime.utcnow() - datetime.timedelta(days=14)

    def _parse_tweet(tweet):
        return {
            'created_at': tweet.created_at,
            'text': tweet.full_text,
            'json': tweet._json
        }

    def _time_filter(tweet):
        return since < tweet['created_at']

    tweets = [_parse_tweet(item) for item in original_tweets]
    tweets = [item for item in tweets if _time_filter(item)]

    return tweets
