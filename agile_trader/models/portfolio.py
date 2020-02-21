class Portfolio:
    def __init__(self, portfolio_data={}):
    	self.name = portfolio_data['name'] if 'name' in portfolio_data else None
    	self.creation_date = portfolio_data['creation_date'] if 'creation_date' in portfolio_data else None
    	self.cash = portfolio_data['cash'] if 'cash' in portfolio_data else None
    	self.total_value = portfolio_data['total_value'] if 'total_value' in portfolio_data else None
    	self.stocks = portfolio_data['stocks'] if 'stocks' in portfolio_data else None # list of Holding objects
        