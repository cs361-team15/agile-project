from util.PayloadParser import PayloadParser
from .RemoteMessageService import RemoteMessageService
from .DaoService import DaoService
from .CacheService import CacheService

class ApplicationService:
    def __init__(self, dao):
        self.dao = dao
        self.cache = CacheService()
        self.handler = RemoteMessageService()
        self.parser = PayloadParser()

    def holdingTest(self):
        return "Testing ApplicationService - returning a Holding object: " + holding.test()

    def handlerTest(self):
        response = self.handler.getStockBatch(['ATVI'])
        result = self.parser.parse(response, 'WTD') 
        return "Testing ApplicationService - returning a handler result:  " + result[0]['symbol']

    def getStockHistory(self):
        pass

    def getStock(self, symbol):
        result = self.cache.find(symbol)
        if not result:
            # pretend not found in DB either
            # result = dao.getStock(symbol)
            if not result:
                result = self.handler.getStockBatch([symbol])
                result = self.parser.parse(result, 'WTD')[0]
            self.cache.add(result)
        return result

# if __name__ == '__main__':
#     appService = ApplicationService()

#     print(appService.getStock('TM'))