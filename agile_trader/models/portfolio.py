class Portfolio:
    def __init__(self, portfolio_data):
    	self.name = portfolio_data['name']
    	self.creation_date = portfolio_data['creation_date']
    	self.cash = portfolio_data['cash']
    	self.total_value = portfolio_data['total_value']
    	self.stocks = portfolio_data['stocks'] # list of Holding objects
        