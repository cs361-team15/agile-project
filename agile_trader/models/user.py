class User:
    def __init__(self, user_data):
        self.email = user_data['email']
        self.password = user_data['password']
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.portfolios = user_data['portfolios']
        self.watchlists = user_data['watchlists']