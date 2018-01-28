import datetime
import time
import requests
import pickle

def parsePrice():
    r = requests.get("https://graphs2.coinmarketcap.com/currencies/bitcoin/1516028059000/1516632859000/") #this address will change, sourced by clicking "1m" on https://coinmarketcap.com/currencies/bitcoin/ and checking the network tab for the referenced source.
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

    #Convert market info to normal times here
    for USDPricePoints in price_usd:
       USDPricePoints[0] = datetime.datetime.fromtimestamp(USDPricePoints[0]/1e3)
    for times in price_usd:
        print(times[0])

    market_info.append(marketCap)
    market_info.append(price_btc)
    market_info.append(price_usd)
    market_info.append(price_usd)
    market_info.append(volume_usd)

   currentTime = datetime.date.today().strftime("%B %d, %Y")

    with open("marketInfo " + currentTime, "wb") as fp:
        pickle.dump(1,fp)

    return market_info
