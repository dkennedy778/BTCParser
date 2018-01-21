from textblob import TextBlob
import math

#More than 50% of the tweets are junk, can't derive any sentiment information from them.
def get_tweet_sentiment(tweets):
    scores = []
    i = 0
    for block in tweets:
        blockScore = 0;
        for tweet in block:
            text = tweet[0]["text"]
            sentiment = TextBlob(text)
            #Testing stuff
            #print(sentiment.polarity)
            if(sentiment.polarity != 0):
                i = i + 1 #incrementing the number of valid tweets in the block
                #weight the score, weighting scale in ln()
                if(int(tweet[0]["retweets"]) > 0):
                    score = sentiment.polarity + math.log(int(tweet[0]["retweets"]), 2.71828)
                else:
                    score = sentiment.polarity
                blockScore = blockScore + score
        blockScore = blockScore/i
        i = 0
        print("BLOCK COMPLETE")
        print(blockScore)
