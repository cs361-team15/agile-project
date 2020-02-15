import requests
import json

class RemoteMessageService:
    def __init__(self):
        pass

    def getStockLongHistory(self, symbol):
        # key = dao.getKey('AV')
        key = 'VUUT2T6MX6AKP991'
        long_history_endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=' + symbol + '&apikey=' + key
        result = requests.get(long_history_endpoint)
        response = result.json()
        # dao.incrementKeyUsage('AV')
        # print(response)

    def getStockBatch(self, symbols):
        # key = dao.getKey('WTD')
        key = 'uo9zAw0g4QeNtJKrmXzMLvlKkvpl03CPYZup39xsZTUisN7qzLjTyQzjEraV'
        batch_endpoint = 'https://api.worldtradingdata.com/api/v1/stock?symbol=' + ','.join(symbols) + '&api_token=' + key
        result = requests.get(batch_endpoint)
        response = result.json()
        # dao.incrementKeyUsage('WTD')
        return response

    
    



#test = RemoteMessageParser()

#symbol1 = 'TM'
#symbol2 = 'MSFT'
#symbol3 = 'AAPL'
#symbol4 = 'GOOGL'
#symbol5 = 'ATVI'
#symbol6 = 'SBUX'
#symbol7 = 'GE'
#symbol8 = 'F'
#symbol9 = 'PG'
#symbol10 = 'DIS'

#symbols = [symbol1, symbol2, symbol3, symbol4, symbol5]

#test.get_stock_long_history(symbol1)