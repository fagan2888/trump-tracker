from fetch import fetch_tweets
from generator import generate
import os
import json
import fire


class Main:
    @staticmethod
    def fetch_tweets(consumer_key='',
                     consumer_secret='',
                     access_token_key='',
                     access_token_secret=''):
        tweets = fetch_tweets(consumer_key, consumer_secret, access_token_key, access_token_secret)
        for tweet in tweets:
            fp = tweet['created_at'].strftime('%Y-%m-%d_%H_%M_%S.json')
            fp = os.path.join('build/cache', fp)
            if not os.path.exists(fp):
                with open(fp, 'w') as f:
                    json.dump(tweet['json'], f, indent=2, sort_keys=True)

    @staticmethod
    def generate():
        generate()


if __name__ == '__main__':
    fire.Fire(Main)
