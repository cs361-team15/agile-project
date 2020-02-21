class Holding:
    def __init__(self, holding_data={}):
        self.ticker = holding_data['ticker'] if 'ticker' in holding_data else None
        self.name = holding_data['name'] if 'name' in holding_data else None
        self.price_history = holding_data['price_history'] if 'price_history' in holding_data else None
        self.open_price = holding_data['open_price'] if 'open_price' in holding_data else None
        self.current_price = holding_data['current_price'] if 'current_price' in holding_data else None
        self.current_volume = holding_data['current_volume'] if 'current_volume' in holding_data else None
        self.market_cap = holding_data['market_cap'] if 'market_cap' in holding_data else None
        self.fifty_two_week_high = holding_data['fifty_two_week_high'] if 'fifty_two_week_high' in holding_data else None
        self.fifty_two_week_low = holding_data['fifty_two_week_low'] if 'fifty_two_week_low' in holding_data else None

    def test(self):
        return "Testing Holding class"