import datetime
import json
import queue

class CacheService:
    def __init__(self, timeout=10, cache_size=100):
        self.dict_file = 'cache/dictionary.json'
        self.queue_file = 'cache/queue.txt'
        self.timeout = datetime.timedelta(minutes=timeout) # minutes
        self.cache_size = cache_size
        self.dict = None
        self._load()

    def _load(self):
        with open(self.dict_file) as infile:
            try:
                self.dict = json.load(infile)
            except json.JSONDecodeError:
                self.dict = {}

    def _save(self):
        with open(self.dict_file, 'w') as outfile:
            json.dump(self.dict, outfile)

    def _purgeOld(self):
        keys = [key for key in self.dict]
        for symbol in keys:
            if datetime.datetime.now() - datetime.datetime.strptime(self.dict[symbol]['date'], "%Y-%m-%d %H:%M:%S.%f") >= self.timeout:
                self.dict.pop(symbol)
        self._save()

    def find(self, symbol):
        self._purgeOld()
        if not symbol in self.dict:
            return None
        return self.dict[symbol]

    def _findOldest(self):
        oldest = (None, datetime.timedelta(seconds=0))
        for symbol in self.dict:
            age = datetime.datetime.now() - datetime.datetime.strptime(self.dict[symbol]['date'], "%Y-%m-%d %H:%M:%S.%f")
            if age > oldest[1]:
                oldest = (symbol, age)
        return oldest[0]

    def add(self, stock_data):
        self.dict[stock_data['symbol']] = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            'name': stock_data['name'],
            'market_cap': stock_data['market_cap'],
            'open_price': stock_data['open_price'],
            'price': stock_data['price'],
            'day_high': stock_data['day_high'],
            'day_low': stock_data['day_low'],
            'fifty_two_week_high': stock_data['fifty_two_week_high'],
            'fifty_two_week_low': stock_data['fifty_two_week_low']
        }
        if len(self.dict) >= self.cache_size:
            self.dict.pop(self._findOldest())
        self._save()

# if __name__ == '__main__':
#     cs = CacheService()

#     print(cs.find('TM'))

#     cs.add({'symbol': 'TM', 
#         'name': 'Toyota', 
#         'market_cap': '10000000000', 
#         'open_price': '52.02', 
#         'price': '53.44', 
#         'day_high': '54.05', 
#         'day_low': '51.78', 
#         'fifty_two_week_high': '63.02', 
#         'fifty_two_week_low': '47.58'
#     })    

#     print(cs.find('TM'))

#     cs.add({'symbol': 'F', 
#         'name': 'Ford', 
#         'market_cap': '10000000000', 
#         'open_price': '52.02', 
#         'price': '53.44', 
#         'day_high': '54.05', 
#         'day_low': '51.78', 
#         'fifty_two_week_high': '63.02', 
#         'fifty_two_week_low': '47.58'
#     })  

#     cs.add({'symbol': 'GM', 
#         'name': 'General Motors', 
#         'market_cap': '10000000000', 
#         'open_price': '52.02', 
#         'price': '53.44', 
#         'day_high': '54.05', 
#         'day_low': '51.78', 
#         'fifty_two_week_high': '63.02', 
#         'fifty_two_week_low': '47.58'
#     })  

#     print(cs._findOldest())