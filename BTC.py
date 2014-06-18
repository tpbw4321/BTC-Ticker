import json
import requests
import os

usdCnyRatioAPI = 'http://www.freecurrencyconverterapi.com/api/convert?q=CNY-USD'
btceBtcAPI = 'https://btc-e.com/api/2/btc_usd/ticker'
btceLtcAPI = 'https://btc-e.com/api/2/ltc_usd/ticker'
btceXpmAPI = 'https://btc-e.com/api/2/xpm_btc/ticker'
huobiBtcAPI = 'http://market.huobi.com/staticmarket/ticker_btc_json.js'

def btceAPI(API):
	btceTick = requests.get(API)
	return btceTick.json()['ticker']['last']

def getUsdCnyRatio():
	usdCnyRatio = requests.get(usdCnyRatioAPI)
	return usdCnyRatio.json()['results']['CNY-USD']['val']

while True :
	btceBtc = float(btceAPI(btceBtcAPI))
	btceLtc = float(btceAPI(btceLtcAPI))
	btceXpm = float(btceAPI(btceXpmAPI))
	huobiBtc = float(btceAPI(huobiBtcAPI))
	usdCnyRatio = getUsdCnyRatio()

	os.system('clear')
	print "BTC/USD"
	print "BTC-e: ", btceBtc
	print "Huobi: ", float(huobiBtc*usdCnyRatio)
	print
	print "LTC/USD"
	print "BTC-e: ", btceLtc
	print
	print "XPM/BTC"
	print "BTC-e: ", btceXpm
