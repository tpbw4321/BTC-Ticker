import json
import requests
import os

usdCnyRatioAPI = 'http://www.freecurrencyconverterapi.com/api/convert?q=CNY-USD'
btcUsd = 'btc_usd'
ltcUsd = 'ltc_usd'
ethBtc = 'eth_btc'
ltcBtc = 'ltc_btc'
btceURL = 'https://btc-e.com/api/3/ticker/'
#updated to work with new BTC-E api, feel free to add your desired ratio

def btceAPI(URL,uType):
	btceTick = requests.get(URL+uType)
	return btceTick.json()[uType]['last']

def getUsdCnyRatio():
	usdCnyRatio = requests.get(usdCnyRatioAPI)
	return usdCnyRatio.json()['results']['CNY-USD']['val']

while True :
    btceBtcUsd = float(btceAPI(btceURL,btcUsd))
    btceLtcUsd = float(btceAPI(btceURL,ltcUsd))
    btceEthBtc = float(btceAPI(btceURL,ethBtc))
    btceLtcBtc = float(btceAPI(btceURL,ltcBtc))

    
    os.system('clear')
    print "BTC/USD"
    print "BTC-e: ", btceBtcUsd
    print
    print "LTC/USD"
    print "BTC-e: ", btceLtcUsd
    print
    print "LTC/BTC"
    print "BTC-e: ", btceLtcBtc
    print
    print "ETH/BTC"
    print "BTC-e: ", btceEthBtc
