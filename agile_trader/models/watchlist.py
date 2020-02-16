class Watchlist:
    def __init__(self, watchlist_data={}):
        self.name = watchlist_data['name'] if 'name' in watchlist_data else None
        self.creation_date = watchlist_data['creation_date'] if 'creation_date' in watchlist_data else None
        self.stocks = watchlist_data['stocks'] if 'stocks' in watchlist_data else None