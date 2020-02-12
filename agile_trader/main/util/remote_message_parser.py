import requests
import json
import datetime

class RemoteMessageParser:
    def __init__(self):
        pass

    def get_stock_long_history(self, symbol):
        # key = dao.getKey('AV')
        key = 'VUUT2T6MX6AKP991'
        long_history_endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=' + symbol + '&apikey=' + key
        result = requests.get(long_history_endpoint)
        response = result.json()
        # dao.incrementKeyUsage('AV')
        self.parse(response['Time Series (Daily)'])
        # print(response)

    def get_stock_batch(self, symbols):
        # key = dao.getKey('WTD')
        key = 'uo9zAw0g4QeNtJKrmXzMLvlKkvpl03CPYZup39xsZTUisN7qzLjTyQzjEraV'
        batch_endpoint = 'https://api.worldtradingdata.com/api/v1/stock?symbol=' + ','.join(symbols) + '&api_token=' + key
        result = requests.get(batch_endpoint)
        response = result.json()
        # dao.incrementKeyUsage('WTD')
        self.parse(response['data'], 'WTD')
        print(response)
    
    def parse(self, payload, service='AV'):
        if service == 'AV':
            result = 0
            high = float('-inf')
            low = float('inf')
            today = list(payload)[0]
            year, month, day = today.split('-')
            today = datetime.date(year, month, day)
            cur = today
            past_date = datetime.date(year-1, month, day)
            i = 0
            while cur > past_date:
                cur = list(payload)[i]
                if payload[cur]['high'] > high:
                    high = payload[cur]['high']
                if payload[cur]['low'] < low:
                    low = payload[cur]['low']
                i += 1
                year, month, day = cur.split('-')
                cur = datetime.date(year, month, day)
                
            
            return print(payload[list(payload)[0]])
        else:
            result = []
            for stock in payload:
                result.append({
                    'symbol': stock['symbol'],
                    'name': stock['name'],
                    'market_cap': stock['market_cap'],
                    'open_price': stock['price_open'],
                    'price': stock['price'],
                    'day_high': stock['day_high'],
                    'day_low': stock['day_low'],
                    'fifty_two_week_high': stock['52_week_high'],
                    'fifty_two_week_low': stock['52_week_low']
                })
            return result



test = RemoteMessageParser()

symbol1 = 'TM'
symbol2 = 'MSFT'
symbol3 = 'AAPL'
symbol4 = 'GOOGL'
symbol5 = 'ATVI'
symbol6 = 'SBUX'
symbol7 = 'GE'
symbol8 = 'F'
symbol9 = 'PG'
symbol10 = 'DIS'

symbols = [symbol1, symbol2, symbol3, symbol4, symbol5]

test.get_stock_long_history(symbol1)