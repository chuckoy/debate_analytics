# Import the necessary methods from tweepy library
from tweepy.api import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
from tokens import (
    access_token, access_token_secret, consumer_key, consumer_secret)

from debate_analytics import DebateAnalytics

# This is a basic listener that just prints received tweets to stdout.


class StatusListener(StreamListener):
    """
    Listens to Twitter and sends notification to observers registered to it
    when a new tweet comes along
    """

    def __init__(self, api=None):
        self.api = api or API()
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)
        print "STOP STALKING ME"

    # When we get a new status, call the notify_new_status method of all
    # registered observers and pass the status to them
    def on_data(self, status):
        try:
            for observer in self.__observers:
                observer.notify_new_status(status)
            return
        except:
            pass

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter
    # Streaming API
    l = StatusListener()
    debate_analytics = DebateAnalytics(l)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords:
    stream.filter(track=['#MIRIAM2016', '#Duterte2016',
                         '#RoxasRobredo2016', '#OnlyBinay', '#POE2016'])

    # Create an instance of the analyser and register it as a listener to our
    # StatusListener
