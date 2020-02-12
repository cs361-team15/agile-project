class Stock:
    def __init__(self, stock_data):
        self.symbol = stock_data['symbol']
        self.name = stock_data['name']
        self.market_cap = stock_data['market_cap']
        self.open_price = stock_data['open_price']
        self.price = stock_data['price']
        self.day_high = stock_data['day_high']
        self.day_low = stock_day['day_low']
        self.fifty_two_week_high = stock_data['fifty_two_week_high']
        self.fifty_two_week_low = stock_data['fifty_two_week_low']

    @property
    def day_change(self):
        return self.open_price - self.price