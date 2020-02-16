class User:
    def __init__(self, user_data={}):
        self.email = user_data['email'] if 'email' in user_data else None
        self.password = user_data['password'] if 'password' in user_data else None
        self.first_name = user_data['first_name'] if 'first_name' in user_data else None
        self.last_name = user_data['last_name'] if 'last_name' in user_data else None
        self.portfolios = user_data['portfolios'] if 'portfolios' in user_data else None
        self.watchlists = user_data['watchlists'] if 'watchlists' in user_data else None