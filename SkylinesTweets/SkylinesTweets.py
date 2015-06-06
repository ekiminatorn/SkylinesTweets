#!/usr/bin/python
"""
--TODO--
Nothing at the moment
"""
import tweepy

VERSION_NUMBER = '1.0.0'

"""
SEMANTIC VERSIONING:
1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards-compatible bug fixes.
"""

import twatter,time
from ConfigParser import SafeConfigParser
from random import randint
from datetime import datetime, timedelta

#Initial starting up stuff
print '-----------------------------'
print 'Reading config'
configparser = SafeConfigParser()
configparser.read('config.cfg')

#Twitter Credentials
TWITTER_CONSUMER_KEY = configparser.get('TWITTER_CREDENTIALS', 'consumer_key')
TWITTER_CONSUMER_SECRET = configparser.get('TWITTER_CREDENTIALS', 'consumer_secret')
TWITTER_ACCESS_TOKEN = configparser.get('TWITTER_CREDENTIALS', 'access_token')
TWITTER_ACCESS_TOKEN_SECRET = configparser.get('TWITTER_CREDENTIALS', 'access_token_secret')

#How many lines (Tweets) we have in storage
num_lines = sum(1 for line in open('tweets'))
print "We have %s tweets in storage. To add more, stop this program and add them manually to the file!" % num_lines
num_lines -= 1

print 'Reading config complete. Starting loop'
print '-----------------------------'


#Program starts here (loop) until forced to close.
while True:
    
    time.sleep(5)
    
    tweet = twatter.get_random_tweet(num_lines)
    
    try:
        twatter.tweet(tweet, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    except tweepy.TweepError as e:
        print 'ERROR! Error message below:'
        print e.message[0]['message']
        pass
    #Randomly selects new time to post between 2h - 6h
    sleepTime = randint(7200, 21600)
    
    sec = timedelta(seconds=int(sleepTime))
    d = datetime(1,1,1) + sec


    print ("Sleeping for %d hours, %d minutes and %d seconds" % (d.hour, d.minute, d.second))
    time.sleep(sleepTime)
   
    
    

