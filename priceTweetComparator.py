
def comparePricesandTwitter(marketInfo, sentiments):

    #Get % change for prices over period
    initialPrice = marketInfo[2][1][1] #USD price changes are the last list in the master list, prices are the first index
    priceMovements = []
    for prices in marketInfo[2]:
        priceMovements.append(get_change(initialPrice,prices[1]))
        initialPrice = prices[1]

    #Get % change for twitter over period
    sentimentMovements = []
    initialSentiment = sentiments[0]
    for sentiment in sentiments:
        sentimentMovements.append(get_change(initialSentiment,sentiment[0]))
        initialSentiment = sentiments[0]

    #Compare the two lists
    #May be worth ordering the sentiment blocks by the marketplace time periods given by coincap

def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
       return ((abs(current - previous))/previous)*100.0
    except ZeroDivisionError:
        return 0
