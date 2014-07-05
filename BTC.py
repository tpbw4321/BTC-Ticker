import json
import requests
import os

usdCnyRatioAPI = 'http://www.freecurrencyconverterapi.com/api/convert?q=CNY-USD'
btceBtcUsdAPI = 'https://btc-e.com/api/2/btc_usd/ticker'
btceLtcUsdAPI = 'https://btc-e.com/api/2/ltc_usd/ticker'
btceXpmBtcAPI = 'https://btc-e.com/api/2/xpm_btc/ticker'
btceLtcBtcAPI = 'https://btc-e.com/api/2/ltc_btc/ticker'
huobiBtcCnyAPI = 'http://market.huobi.com/staticmarket/ticker_btc_json.js'

def btceAPI(API):
	btceTick = requests.get(API)
	return btceTick.json()['ticker']['last']

def getUsdCnyRatio():
	usdCnyRatio = requests.get(usdCnyRatioAPI)
	return usdCnyRatio.json()['results']['CNY-USD']['val']

while True :
    btceBtcUsd = float(btceAPI(btceBtcUsdAPI))
    btceLtcUsd = float(btceAPI(btceLtcUsdAPI))
    btceXpmBtc = float(btceAPI(btceXpmBtcAPI))
    btceLtcBtc = float(btceAPI(btceLtcBtcAPI))
    huobiBtcCny = float(btceAPI(huobiBtcCnyAPI))
    usdCnyRatio = getUsdCnyRatio()
    
    os.system('clear')
    print "BTC/USD"
    print "BTC-e: ", btceBtcUsd
    print "Huobi: ", float(huobiBtcCny*usdCnyRatio)
    print
    print "LTC/USD"
    print "BTC-e: ", btceLtcUsd
    print
    print "LTC/BTC"
    print "BTC-e: ", btceLtcBtc
    print
    print "XPM/BTC"
    print "BTC-e: ", btceXpmBtc
