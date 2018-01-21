import json
from pprint import pprint
import datetime
import logging
import collections

tweetAndTime = collections.namedtuple('tweet','dateTime')


JSONParser_logger = logging.getLogger('memeMaker')
namesList = []
def parseTweets(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
        JSONParser_logger.info('loaded data file ' + str(data_file))
    pprint("start")
    #Goal here is to order tweets by time, shooting for blocks of one hour right now
    times = []
    #Want to sort the tweets with datetime objects, so here I'm just parsing through all of the tweets and converting their timestamps to datetime objects. I then store all tweets with their datetime objects into a tuple, which I put into a list of tuples.
    #This'll make sorting easier, but imposes an immediate O(N) performance cost, which may be significant with large tweet batches.

    try:
        for dataPoint in data:
            Strtime = dataPoint["timestamp"]
            tweetTime = datetime.datetime.strptime(Strtime, "%Y-%m-%dT%H:%M:%S")
            tweetToBeStored = (dataPoint,tweetTime)
            times.append(tweetToBeStored)
        #Now we have all of our tweets stored, lets sort them by their datetimes
        times.sort(key=lambda tup: tup[1])

    #Next task is to split up tweets into blocks of ten minutes based on their date time
        startTweet = times[0]
        startTime = startTweet[1]
        sortedTweets = []
        TenMinBlockTweets = []
        for tweet in times:
         #Delta is the difference between the inital time and 
         delta = tweet[1] - startTime
         if (delta <= datetime.timedelta(minutes=10)): #funny bug here, can't compare a timedelta to an int, need to cast the int as a new timedelta
            TenMinBlockTweets.append(tweet)
         else:
             sortedTweets.append(TenMinBlockTweets)
             TenMinBlockTweets = []
             startTime = tweet[1]

    except Exception as e:
        JSONParser_logger.exception("exception hit")