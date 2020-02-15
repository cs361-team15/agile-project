import datetime

class PayloadParser:
    def __init__(self):
        pass

    def parse(self, payload, service='AV'):
        if service == 'AV':
            result = 0
            high = float('-inf')
            low = float('inf')
            today = list(payload)[0]
            year, month, day = today.split('-')
            today = datetime.date(year, month, day)
            cur = today
            past_date = datetime.date(year-1, month, day)
            i = 0
            while cur > past_date:
                cur = list(payload)[i]
                if payload[cur]['high'] > high:
                    high = payload[cur]['high']
                if payload[cur]['low'] < low:
                    low = payload[cur]['low']
                i += 1
                year, month, day = cur.split('-')
                cur = datetime.date(year, month, day)
                       
            return print(payload[list(payload)[0]])
        else:
            result = []
            for stock in payload['data']:
                result.append({
                    'symbol': stock['symbol'],
                    'name': stock['name'],
                    'market_cap': stock['market_cap'],
                    'open_price': stock['price_open'],
                    'price': stock['price'],
                    'day_high': stock['day_high'],
                    'day_low': stock['day_low'],
                    'fifty_two_week_high': stock['52_week_high'],
                    'fifty_two_week_low': stock['52_week_low']
                })
            return result