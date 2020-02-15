class Watchlist:
    def __init__(self, watchlist_data):
        self.name = watchlist_data['name']
        self.creation_date = watchlist_data['creation_date']
        self.stocks = watchlist_data['stocks']