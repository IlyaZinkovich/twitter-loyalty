from TwitterSearch import *
import sys
import json
import datetime

keywords = sys.argv[1:]
print('Searching twitter for ' + str(keywords))

tso = TwitterSearchOrder()
tso.set_keywords(keywords, or_operator = True)

ts = TwitterSearch(
    consumer_key = '82OeTtCHbvyHPWq5pwZrIWKba',
    consumer_secret = '2WgxdRrDyT1k980s8L1progwyfnnKhQIcWq4F114kcbaTdq8bT',
    access_token = '2874250521-Y06ljPTPZCHzbtOcBJKKhHYArH0NkOdSBh33TQc',
    access_token_secret = 'RhFkv8LQhHpOH2cvfBNfQPOnpFssuy0HQPQ8ttoLE3uzz'
)
data = { 'date' : datetime.datetime.now().date().isoformat() }
tweets = []
for tweet in ts.search_tweets_iterable(tso):
    tweets.append(tweet)
data['tweets'] = tweets
with open(data['date'], 'w') as outfile:
    json.dump(data, outfile)
