class Record:
    def __init__(self, record_data):
        self.date = record_data['date']
        self.price = record_data['price']
        self.volume = record_data['volume']