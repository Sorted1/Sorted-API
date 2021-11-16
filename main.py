from flask import *
import json, time
import random, requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set ={'page': 'Home', 'Message': 'Hello World', 'Timestamp': time.localtime()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/user/', methods=['GET'])
def request_page ():
    user_query = str(request.args.get('user')) # /user/?user=USER_NAME

    message=f'{user_query}'
    
    json_dump = json.dumps (message)
    
    return json_dump

@app.route('/random/', methods=['GET'])
def math_page():

    num = random.randint(1, 999999999999)

    json_dump = json.dumps(num)

    return json_dump

@app.route('/btc/', methods=['GET'])
def btc_page():

    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']

    price = f'{str(usd)}'

    json_dump = json.dumps(price)

    return json_dump

if __name__ == '__main__':
    app.run(port=8888)