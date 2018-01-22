import datetime
import requests

#Parses price information from a fixed URL
def parsePrice():
    r = requests.get("https://graphs2.coinmarketcap.com/currencies/bitcoin/") #this address may change
    marketCap = []
    price_btc = []
    price_usd = []
    volume_usd = []
    market_info = []

    response_data = r.json()
    
    for data in response_data["market_cap_by_available_supply"]:
        marketCap.append(data)
    print("market cap done")
    for data in response_data["price_btc"]:
        price_btc.append(data)
    print("price btc done")
    for data in response_data["price_usd"]:
        price_usd.append(data)
    print("price USD done")
    for data in response_data["volume_usd"]:
        volume_usd.append(data)
    print("volume done")
    
    #Price data is in format (time, amount). The meaning of the amount field varies by datatype 
    for USDPricePoints in price_usd:
       date = datetime.datetime.fromtimestamp(USDPricePoints[0]/1e3) #see https://stackoverflow.com/questions/9744775/how-to-convert-integer-timestamp-to-python-datetime
       print(date)

    market_info.append(marketCap)
    market_info.append(price_btc)
    market_info.append(price_usd)
    market_info.append(volume_usd)

    return market_info
