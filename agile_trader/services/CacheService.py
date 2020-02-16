import datetime
import json
import queue

class CacheService:
    def __init__(self, timeout=10, cache_size=100):
        self.dict_file = 'cache/dictionary.json'
        self.queue_file = 'cache/queue.txt'
        self.timeout = timeout # minutes
        self.cache_size = cache_size
        self.dict = None
        self.queue = queue.Queue()
        self._load()

    def _load(self):
        with open(self.dict_file) as infile:
            self.dict = json.load(infile)
        with open(self.queue_file) as infile:
            for line in infile:
                self.queue.put(line)

    def _save(self):
        with open(self.dict_file, 'w') as outfile:
            json.dump(self.dict, outfile)
        with open(self.queue_file, 'w') as outfile:
            for symbol in self.queue:
                outfile.write(symbol)

    def purgeOld(self, symbol):
        if not symbol in self.dict():
            return
        while self.queue.pop() != symbol:
            self.dict.remove(symbol)

    def find(self, symbol):
        if not symbol in self.dict():
            return None
        data = self.dict[symbol]
        if datetime.now() - datetime.strptime(data['date'], "%Y-%m-%d %H:%M:%S.%f") >= self.timeout():
            self.purgeOld(symbol)
            self._save()
            return None
        return data

    def add(self, stock_data):
        self.cache[stock_data['symbol']] = {
            'date': datetime.now(),
            'name': stock_data['name'],
            'market_cap': stock_data['market_cap'],
            'open_price': stock_data['open_price'],
            'price': stock_data['price'],
            'day_high': stock_data['day_high'],
            'day_low': stock_data['day_low'],
            'fifty_two_week_high': stock_data['fifty_two_week_high'],
            'fifty_two_week_low': stock_data['fifty_two_week_low']
        }
        if len(self.queue) >= self.cache_size:
            self.dict.remove(self.queue.pop())
        self.queue.put(stock_data['symbol'])
        self._save()

