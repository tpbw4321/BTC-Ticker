import json
import requests
import os

btceBtcAPI = 'https://btc-e.com/api/2/btc_usd/ticker'
btceLtcAPI = 'https://btc-e.com/api/2/ltc_usd/ticker'
btceXpmAPI = 'https://btc-e.com/api/2/xpm_btc/ticker'
goxBTC = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast'

def btceAPI(API):
	btceTick = requests.get(API)
	return btceTick.json()['ticker']['last']


while True :
	btceBtc = float(btceAPI(btceBtcAPI))
	btceLtc = float(btceAPI(btceLtcAPI))
	btceXpm = float(btceAPI(btceXpmAPI))

	os.system('clear')
	print "BTC/USD"
	print "BTC-e: ", btceBtc
	print
	print "LTC/USD"
	print "BTC-e: ", btceLtc
	print
	print "XPM/BTC"
	print "BTC-e: ", btceXpm


