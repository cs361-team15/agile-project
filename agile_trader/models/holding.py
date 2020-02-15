class Holding:
    def __init__(self, holding_data):
        self.ticker = holding_data['ticker']
        self.name = holding_data['name']
        self.price_history = holding_data['price_history'] # List of Records
        self.open_price = holding_data['open_price']
        self.current_price = holding_data['current_price']
        self.current_volume = holding_data['current_volume']
        self.market_cap = holding_data['market_cap']
        self.fifty_two_week_high = holding_data['fifty_two_week_high']
        self.fifty_two_week_low = holding_data['fifty_two_week_low']

    def test(self):
        return "Testing Holding class"