
from JSONParser import *
import logging
import JSONParser
import datetime

#Building the top level logger
logger = logging.getLogger('memeMaker')
logger.setLevel(logging.DEBUG)
#building a file handler which will log practically everything
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
#Console handler has a more critical logging level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# Creating a formatter which includes the time, program name, class name, and any messages.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('program beginning execution at ' + str(datetime.datetime.now()))

#This loop will be continuously run by a powershell script. JSONParser is not currently called but when I start running this on a continous loop it will be run as tweet parsing is completed
logger.info('Parsing JSON data')
#Parsing goes here
logger.info('JSON data parsed')
filename = 'sampleData.json'

#initializing return lists
tweetsToMeme = []
picURLs = []

logger.info('populating meme tweets and pic URL lists')
tweetsToMeme, picURLs = parseTweets(filename)
logger.info('lists successfully populated')
#Sentiment analysis goes here!
logger.info('Execution completed at ' + str(datetime.datetime.now()))
