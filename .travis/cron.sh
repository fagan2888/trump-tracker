#!/bin/sh
python3 core/core.py fetch_tweets $CONSUMER_KEY $CONSUMER_SECRET $ACCESS_TOKEN_KEY $ACCESS_TOKEN_SECRET
python3 core/core.py generate
