import datetime
import json

class CacheService:
    def __init__(self, timeout=600, cache_size=100):
        self.dict_file = 'cache/dictionary.json'
        self.timeout = datetime.timedelta(seconds=timeout)
        self.cache_size = cache_size
        self.cache = None
        self._load()

    def _purgeAll(self):
        self.cache = {}
        self._save()

    def _load(self):
        with open(self.dict_file) as infile:
            try:
                self.cache = json.load(infile)
            except json.JSONDecodeError:
                self.cache = {}

    def _save(self):
        with open(self.dict_file, 'w') as outfile:
            json.dump(self.cache, outfile)

    def _purgeOld(self):
        keys = [key for key in self.cache]
        for symbol in keys:
            if datetime.datetime.now() - datetime.datetime.strptime(self.cache[symbol]['date'], "%Y-%m-%d %H:%M:%S.%f") >= self.timeout:
                self.cache.pop(symbol)
        self._save()

    def _findOutdated(self):
        '''
        Summary:    Returns the oldest symbol in the cache if that entry's age is greater than the cache timeout,
                    otherwise returns the symbol of the entry with the longest time since it was accessed. 
        Params:     None.
        Outputs:    [1] string representing a stock symbol.
        '''
        oldestCreationTime = (None, datetime.timedelta(seconds=0))
        oldestAccessTime = (None, datetime.timedelta(seconds=0))
        currentTime = datetime.datetime.now()
        for symbol in self.cache:
            age = currentTime - datetime.datetime.strptime(self.cache[symbol]['date'], "%Y-%m-%d %H:%M:%S.%f")
            print(age)
            timeSinceAccess = currentTime - datetime.datetime.strptime(self.cache[symbol]['last_accessed'], "%Y-%m-%d %H:%M:%S.%f")
            if age > oldestCreationTime[1]:
                oldestCreationTime = (symbol, age)
            if timeSinceAccess > oldestAccessTime[1]:
                oldestAccessTime = (symbol, timeSinceAccess)
        return oldestCreationTime[0] if oldestCreationTime[1] > self.timeout else oldestAccessTime[0]

    def find(self, symbol):
        self._purgeOld()
        if not symbol in self.cache:
            return None
        self.cache[symbol]['last_accessed'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return self.cache[symbol]

    def add(self, stock_data):
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.cache[stock_data['symbol']] = {
            'date': currentTime,
            'last_accessed': currentTime,
            'name': stock_data['name'],
            'market_cap': stock_data['market_cap'],
            'open_price': stock_data['open_price'],
            'price': stock_data['price'],
            'day_high': stock_data['day_high'],
            'day_low': stock_data['day_low'],
            'fifty_two_week_high': stock_data['fifty_two_week_high'],
            'fifty_two_week_low': stock_data['fifty_two_week_low']
        }
        if len(self.cache) > self.cache_size:
            self.cache.pop(self._findOutdated())
        self._save()

if __name__ == '__main__':
    cs = CacheService()

    print(cs.find('TM'))

    cs.add({'symbol': 'TM', 
        'name': 'Toyota', 
        'market_cap': '10000000000', 
        'open_price': '52.02', 
        'price': '53.44', 
        'day_high': '54.05', 
        'day_low': '51.78', 
        'fifty_two_week_high': '63.02', 
        'fifty_two_week_low': '47.58'
    })    

    print(cs.find('TM'))

    cs.add({'symbol': 'F', 
        'name': 'Ford', 
        'market_cap': '10000000000', 
        'open_price': '52.02', 
        'price': '53.44', 
        'day_high': '54.05', 
        'day_low': '51.78', 
        'fifty_two_week_high': '63.02', 
        'fifty_two_week_low': '47.58'
    })  

    cs.add({'symbol': 'GM', 
        'name': 'General Motors', 
        'market_cap': '10000000000', 
        'open_price': '52.02', 
        'price': '53.44', 
        'day_high': '54.05', 
        'day_low': '51.78', 
        'fifty_two_week_high': '63.02', 
        'fifty_two_week_low': '47.58'
    })  

    print(cs._findOutdated())