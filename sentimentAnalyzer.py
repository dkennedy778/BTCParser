from textblob import TextBlob
import math

#More than 50% of the tweets are junk, can't derive any sentiment information from them.
def get_tweet_sentiment(tweets):
    scores = []
    validTweetsPerBlock = 0
    for block in tweets:
        blockScore = 0;
        for tweet in block:
            text = tweet[0]["text"]
            sentiment = TextBlob(text)
            #Testing stuff
            #print(sentiment.polarity)
            if(sentiment.polarity != 0):
                validTweetsPerBlock = validTweetsPerBlock + 1 #incrementing the number of valid tweets in the block
                #weight the score, weighting scale in ln()
                if(int(tweet[0]["retweets"]) > 0):
                    score = sentiment.polarity + math.log(int(tweet[0]["retweets"]), 2.71828)
                    #blockScore = blockScore + score
                else:
                    score = sentiment.polarity
                    #blockScore = blockScore + score
                blockScore = blockScore + score
        blockScore = blockScore/validTweetsPerBlock
        validTweetsPerBlock = 0
        print("BLOCK COMPLETE")
        print(blockScore)
        scores.append(blockScore)
    return scores
