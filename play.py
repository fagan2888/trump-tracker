import twitter
import datetime

since = datetime.datetime.utcnow() - datetime.timedelta(days=14)


def parse_tweet(tweet):
    created_at = datetime.datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y')
    text = tweet.text
    return {'created_at': created_at, 'text': text}


def time_filter(tweet):
    return since < tweet['created_at']


api = twitter.Api(consumer_key='ob7kYQzbydbo9pj3Btg8rivaZ',
                  consumer_secret='uWlivbYgxA0SAz84bmtjy9dg3l1SMib7Jm2IapuXU2Xj0WrMbW',
                  access_token_key='931209924385710080-s0KdXFYbfM6Ovd9yW5nigjznwkwJwCA',
                  access_token_secret='qHpVCURgIIB4T0FfCmi1ksprL7zvpk9s3JOE3iPF5inIw')

statuses = api.GetUserTimeline(screen_name='realDonaldTrump')
statuses = [parse_tweet(item) for item in statuses]
statuses = [parse_tweet(item) for item in statuses if time_filter(item)]
for item in statuses:
    print(item)
