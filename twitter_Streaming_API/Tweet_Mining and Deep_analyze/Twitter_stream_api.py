#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
consumer_key = 'vmYHpTCOo34lqzrWSkdnhyd10'
# put your consumer_secret from Twitter API
consumer_secret = '4yR2GHiLQoKh71GDZgVAA8LEIJIuHT2DTMbPoOoV649rHzIpdW'
# put your access_token from Twitter API
access_token = '1008737228166594560-aGuXlq6Uqdg6AsDhGKMPm26eNAjeUV'
# put your access_secret from Twitter API
access_secret = 'h5Xy0Te0lCxmgXLyOFXGwELF29gJtYtvxg5DjW16cgOFG'

#basic listener to print tweet recieved
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self,status):
        print(status)
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: '#worldcup', 
    # 'Luis Suarez', 'Cristiano Ronaldo',
    stream.filter(track=['#worldcup', 'Luis Suarez',
                         'Cristiano Ronaldo','Neymar','Lioçnel Messi'])


