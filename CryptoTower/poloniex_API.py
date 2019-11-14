import requests
import json
import hashlib,hmac
import urllib
import time
import config

s = requests.Session()

def get_course():
    url = "https://poloniex.com/public?command=returnTicker"
    respons = s.get(url)
    data = json.loads(respons.text)
    return data

def get_history():
    url = "https://poloniex.com/public?command=return24hVolume"
    respons = s.get(url)
    data = json.loads(respons.text)
    return data

def api_query(command, req = {}):
    req['command'] = command
    req['nonce'] = int(time.time()*1000)
    post_data = urllib.parse.urlencode(req)

    sign = hmac.new(config.poloniex_sign,post_data.encode('utf-8'), hashlib.sha512).hexdigest()

    headers1 = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Key' : config.poloniex_key,
        'Sign' : sign
    }

    respons = s.post('https://poloniex.com/tradingApi', data=post_data,headers=headers1)
    data = json.loads(respons.text)
    return data