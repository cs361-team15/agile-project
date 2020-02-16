from ..models import *
from ..util import *
from .RemoteMessageService import RemoteMessageService
from .DaoService import DaoService
from .CacheService import CacheService

# dao = DaoService()
cache = CacheService()
handler = RemoteMessageService()
parser = PayloadParser()
holding = Holding({})

class ApplicationService:
    def __init__(self):
        pass

    def holdingTest(self):
        return "Testing ApplicationService - returning a Holding object: " + holding.test()

    def handlerTest(self):
        response = handler.getStockBatch(['TM'])
        result = parser.parse(response, 'WTD') 
        return "Testing ApplicationService - returning a handler result:  " + result[0]['symbol']
