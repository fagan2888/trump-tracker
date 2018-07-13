#!/bin/sh
git clone https://github.com/Luolc/trump-tracker.git --branch gh-pages --depth 1
mv trump-tracker build
rm -rf build/.git
python3 core/core.py fetch_tweets $CONSUMER_KEY $CONSUMER_SECRET $ACCESS_TOKEN_KEY $ACCESS_TOKEN_SECRET
python3 core/core.py generate
