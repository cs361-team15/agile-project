from ..models import *
from ..util import *

handler = RemoteMessageHandler()
parser = PayloadParser()
holding = Holding()

class ApplicationService:
    def __init__(self):
        pass

    def holding_test(self):
        return "Testing ApplicationService - returning a Holding object: " + holding.test()

    def handler_test(self):
        response = handler.get_stock_batch(['TM'])
        result = parser.parse(response, 'WTD') 
        return "Testing ApplicationService - returning a handler result:  " + result[0]['symbol']