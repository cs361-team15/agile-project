class Stock:
    def __init__(self, stock_data={}):
        self.symbol = stock_data['symbol'] if 'symbol' in stock_data else None
        self.name = stock_data['name'] if 'name' in stock_data else None
        self.market_cap = stock_data['market_cap'] if 'market_cap' in stock_data else None
        self.open_price = stock_data['open_price'] if 'open_price' in stock_data else None
        self.price = stock_data['price'] if 'price' in stock_data else None
        self.day_high = stock_data['day_high'] if 'day_high' in stock_data else None
        self.day_low = stock_data['day_low'] if 'day_low' in stock_data else None
        self.fifty_two_week_high = stock_data['fifty_two_week_high'] if 'fifty_two_week_high' in stock_data else None
        self.fifty_two_week_low = stock_data['fifty_two_week_low'] if 'fifty_two_week_low' in stock_data else None

    @property
    def day_change(self):
        return self.open_price - self.price