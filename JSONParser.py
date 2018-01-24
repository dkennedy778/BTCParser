import json
from pprint import pprint
import datetime
import logging
import collections

tweetAndTime = collections.namedtuple('tweet','dateTime')


JSONParser_logger = logging.getLogger('priceParser')
namesList = []
def parseTweets(filename,marketInfo):
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

        #Price the market data to find the initial sell date and price info
        #In the future we might run the twitterscraper based on this information. For now we'll just assume the user has checked that their tweets correspond to an interval with pertinent price data
        usdPrices = marketInfo[2]
        initialPriceDate = usdPrices[0][0]
        interval = usdPrices[1][0] - initialPriceDate

    #Add a loop that matches up tweet parsing with the start of pricePoints. No point doing this now, I don't have enough data
    #Next task is to split up tweets into blocks that reflect the price data based on their date time
        startTweet = times[0]
        startTime = startTweet[1]
        sortedTweets = []
        TenMinBlockTweets = []
        for tweet in times:
         #Delta is the difference between the inital time and
         delta = tweet[1] - startTime
         if (delta <= interval):
            TenMinBlockTweets.append(tweet)
         else:
             sortedTweets.append(TenMinBlockTweets)
             TenMinBlockTweets = []
             startTime = tweet[1]
        return sortedTweets
    except Exception as e:
        JSONParser_logger.exception("exception hit")
