import unittest
from CacheService import CacheService

class TestCacheService(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        cls.cacheService = CacheService()
        cls.cacheService._purgeAll()

    def testAdd(self):
        symbol = 'F'
        name = 'Ford'
        market_cap = '10000000000'
        open_price = '52.02'
        price = '53.44'
        day_high = '54.05'
        day_low = '51.78'
        fifty_two_week_high = '63.02'
        fifty_two_week_low = '47.58'       
        dummy_data = {'symbol': symbol, 
            'name': name, 
            'market_cap': market_cap, 
            'open_price': open_price, 
            'price': price, 
            'day_high': day_high, 
            'day_low': day_low, 
            'fifty_two_week_high': fifty_two_week_high, 
            'fifty_two_week_low': fifty_two_week_high
        }
        self.cacheService.add(dummy_data)
        self.assertEqual(len(self.cacheService.cache), 1)
        self.assertTrue(symbol in self.cacheService.cache)
        self.assertEqual(self.cacheService.cache[symbol]['name'], dummy_data['name'])
        self.assertEqual(self.cacheService.cache[symbol]['market_cap'], dummy_data['market_cap'])
        self.assertEqual(self.cacheService.cache[symbol]['open_price'], dummy_data['open_price'])
        self.assertEqual(self.cacheService.cache[symbol]['price'], dummy_data['price'])
        self.assertEqual(self.cacheService.cache[symbol]['day_high'], dummy_data['day_high'])
        self.assertEqual(self.cacheService.cache[symbol]['day_low'], dummy_data['day_low'])
        self.assertEqual(self.cacheService.cache[symbol]['fifty_two_week_high'], dummy_data['fifty_two_week_high'])
        self.assertEqual(self.cacheService.cache[symbol]['fifty_two_week_low'], dummy_data['fifty_two_week_low'])

if __name__ == "__main__":
    unittest.main()

