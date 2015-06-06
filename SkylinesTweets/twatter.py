import tweepy
from random import randint

def tweet(tweet, consumer_key, consumer_secret, access_token, access_token_secret):
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    print 'If auth was successful, we should see username now:'
    print(api.me().name)
    
    api.update_status(tweet)
    
def get_random_tweet(num_lines):
    
    data = open('data', 'r')
    last = data.read()
    data.close()
    
    #Generatinf random number, making sure it doesnt match to the last one
    while True:
        randnum = randint(0, num_lines)
        
        
        if randnum != int(last):
            datawrite = open('data', 'w')
            datawrite.write(str(randnum))
            datawrite.close()
            break
        
    #Reads ALL lines from the file
    tweetText = open('tweets', 'r').readlines()
    
    # .rstrip() Strips the newline char away
    return tweetText[randnum].rstrip('\n')
    