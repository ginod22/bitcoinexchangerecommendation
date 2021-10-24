from flask import Flask, jsonify, abort, request, make_response, url_for
from flask import render_template, redirect
import requests

app = Flask(__name__, static_url_path="")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buyorsellbtc')
def buyorsellbtc():
    return render_template('buyorsellbtc.html')

@app.route('/buyorselleth')
def buyorselleth():
    return render_template('buyorselleth.html')

@app.route('/sellbitcoin')
def btcsell():

    #Fetching Data from Coinbase
    coinbase = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    coinbase = coinbase.json()
    coinbase = float(coinbase["data"]["amount"])

    #Fetching Data from Kraken
    kraken = requests.get("https://api.kraken.com/0/public/Ticker?pair=BTCUSD")
    kraken = kraken.json()
    kraken = float(kraken["result"]["XXBTZUSD"]["a"][0])


    if (coinbase > kraken):
        recommendation = "Coinbase"
    elif (kraken > coinbase):
        recommendation = "Kraken"
    else:
        recommendation = "Both are equal"

    return render_template('sellbitcoin.html',cb=coinbase, kr=kraken, rec = recommendation)


@app.route('/sellethereum')
def ethsell():

    #Fetching Data from Coinbase
    coinbase = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    coinbase = coinbase.json()
    coinbase = float(coinbase["data"]["amount"])

    #Fetching Data from kraken
    kraken = requests.get("https://api.kraken.com/0/public/Ticker?pair=ETHUSD")
    kraken = kraken.json()
    kraken = float(kraken["result"]["XETHZUSD"]["a"][0])

    if (coinbase > kraken):
        recommendation = "Coinbase"
    elif (kraken > coinbase):
        recommendation = "Kraken"
    else:
        recommendation = "Both are equal"


    return render_template('sellethereum.html',cb=coinbase, kr=kraken, rec = recommendation)


@app.route('/buybitcoin')
def btcbuy():

    #Fetching Data from Coinbase
    coinbase = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    coinbase = coinbase.json()
    coinbase = float(coinbase["data"]["amount"])

    #Fetching Data from Kraken
    kraken = requests.get("https://api.kraken.com/0/public/Ticker?pair=BTCUSD")
    kraken = kraken.json()
    kraken = float(kraken["result"]["XXBTZUSD"]["a"][0])


    if (coinbase < kraken):
        recommendation = "Coinbase"
    elif (kraken < coinbase):
        recommendation = "Kraken"
    else:
        recommendation = "Both are equal"

    return render_template('buybitcoin.html',cb=coinbase, kr=kraken, rec = recommendation)


@app.route('/buyethereum')
def ethbuy():

    #Fetching Data from Coinbase
    coinbase = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    coinbase = coinbase.json()
    coinbase = float(coinbase["data"]["amount"])

    #Fetching Data from kraken
    kraken = requests.get("https://api.kraken.com/0/public/Ticker?pair=ETHUSD")
    kraken = kraken.json()
    kraken = float(kraken["result"]["XETHZUSD"]["a"][0])

    if (coinbase < kraken):
        recommendation = "Coinbase"
    elif (kraken < coinbase):
        recommendation = "Kraken"
    else:
        recommendation = "Both are equal"


    return render_template('buyethereum.html',cb=coinbase, kr=kraken, rec = recommendation)