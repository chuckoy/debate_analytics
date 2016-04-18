import json
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter


class DebateAnalytics():
    """
    Analyses the statuses sent to it by the StatusListener it registers itself
    into

    :status_listener: the StatusListener that it listens to (listenerInception)
    """

    def __init__(self, status_listener):
        status_listener.register_observer(self)
        self.keywords = ['#MIRIAM2016', '#Duterte2016',
                         '#RoxasRobredo2016', '#OnlyBinay', '#POE2016']
        self.candidates = ['Miriam', 'Duterte', 'Roxas', 'Binay', 'Poe']
        self.candidates_hashtags = dict(zip(self.keywords, self.candidates))
        self.tweet_counts = Counter(self.candidates)
        for candidate in self.candidates:
            self.tweet_counts[candidate] = 0
        print "WE'RE ALL LOADED UP AND READY TO GO"

    def count_tweets(self, tweets_data):
        return len(tweets_data)

    def notify_new_status(self, status):
        # See which candidate/s the tweet is talking about
        tweet = json.loads(status)
        self.update_counts(tweet['text'])

    def update_counts(self, content):
        print content
        for hashtag, candidate in self.candidates_hashtags.items():
            if hashtag.lower() in content.lower():
                self.tweet_counts[candidate] += 1
                print "Hashtag was {}, added 1 to {}".format(hashtag, candidate)

        for candidate, count in self.tweet_counts.items():
            print "{} now has {} number of tweets.".format(candidate, count)
        print "\n"
