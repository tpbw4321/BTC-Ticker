
import json
import urllib2
import os

btceBtc = 'https://btc-e.com/api/2/btc_usd/ticker'
btceLtc = 'https://btc-e.com/api/2/ltc_usd/ticker'
goxBTC = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast'

def getApiData(url) :
    return json.dumps(json.load(urllib2.urlopen(url)))

def parseGox(goxData) :
    start = goxData.find("\"",goxData.find(" ",goxData.find("\"value\":")))
    fin = goxData.find("\"", start+1)
    return goxData[start+1:fin]

def parseBtce(btceData) :
    start = btceData.find(" " , btceData.find("last"))
    fin = btceData.find(",", start)
    return btceData[start:fin]

while True :
    btceBtcData = getApiData(btceBtc)
    btceLtcData = getApiData(btceLtc)
    goxBtcData = getApiData(goxBTC)

    os.system('clear')
    
    print "BTC/USD"
    print "BTC-e: " + parseBtce(btceBtcData)
    print "Mt.Gox: " + parseGox(goxBtcData)
    print "\nLTC/USD"
    print "BTC-e: " + parseBtce(btceLtcData)

