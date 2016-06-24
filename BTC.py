import json
import requests
import os

usdCnyRatioAPI = 'http://www.freecurrencyconverterapi.com/api/convert?q=CNY-USD'
<<<<<<< HEAD
btceBtcUsdAPI = 'https://btc-e.com/api/2/btc_usd/ticker'
btceLtcUsdAPI = 'https://btc-e.com/api/2/ltc_usd/ticker'
btceXpmBtcAPI = 'https://btc-e.com/api/2/xpm_btc/ticker'
btceLtcBtcAPI = 'https://btc-e.com/api/2/ltc_btc/ticker'
huobiBtcCnyAPI = 'http://market.huobi.com/staticmarket/ticker_btc_json.js'
=======
btcUsd = 'btc_usd'
ltcUsd = 'ltc_usd'
ethBtc = 'eth_btc'
ltcBtc = 'ltc_btc'
btceURL = 'https://btc-e.com/api/3/ticker/'
#updated to work with new BTC-E api, feel free to add your desired ratio
>>>>>>> pr/2

def btceAPI(URL,uType):
	btceTick = requests.get(URL+uType)
	return btceTick.json()[uType]['last']

def getUsdCnyRatio():
	usdCnyRatio = requests.get(usdCnyRatioAPI)
	return usdCnyRatio.json()['results']['CNY-USD']['val']

while True :
<<<<<<< HEAD
    btceBtcUsd = float(btceAPI(btceBtcUsdAPI))
    btceLtcUsd = float(btceAPI(btceLtcUsdAPI))
    btceXpmBtc = float(btceAPI(btceXpmBtcAPI))
    btceLtcBtc = float(btceAPI(btceLtcBtcAPI))
    huobiBtcCny = float(btceAPI(huobiBtcCnyAPI))
    usdCnyRatio = getUsdCnyRatio()
=======
    btceBtcUsd = float(btceAPI(btceURL,btcUsd))
    btceLtcUsd = float(btceAPI(btceURL,ltcUsd))
    btceEthBtc = float(btceAPI(btceURL,ethBtc))
    btceLtcBtc = float(btceAPI(btceURL,ltcBtc))

>>>>>>> pr/2
    
    os.system('clear')
    print "BTC/USD"
    print "BTC-e: ", btceBtcUsd
<<<<<<< HEAD
    print "Huobi: ", float(huobiBtcCny*usdCnyRatio)
=======
>>>>>>> pr/2
    print
    print "LTC/USD"
    print "BTC-e: ", btceLtcUsd
    print
    print "LTC/BTC"
    print "BTC-e: ", btceLtcBtc
    print
<<<<<<< HEAD
    print "XPM/BTC"
    print "BTC-e: ", btceXpmBtc
=======
    print "ETH/BTC"
    print "BTC-e: ", btceEthBtc
>>>>>>> pr/2
