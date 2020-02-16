class Record:
    def __init__(self, record_data={}):
        self.date = record_data['date'] if 'date' in record_data else None
        self.price = record_data['price'] if 'price' in record_data else None
        self.volume = record_data['volume'] if 'volume' in record_data else None