import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


class DBminion:

    def __init__(self, u, p, h, db):

        self.DBconfig = {
            'user': u,
            'password': p,
            'host': h,
            'database': db
        }


    def _DB_cxn(self):
        try:
            cxn = mysql.connector.connect(**self.DBconfig)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        return cxn


    def _DB_CUD(self, statement, data):
        cxn = self._DB_cxn()
        cursor = cxn.cursor()
        cursor.execute(statement, data)
        cxn.commit()
        cursor.close()
        cxn.close()

    
    def _DB_R(self, statement, data):
        cxn = self._DB_cxn()
        cursor = cxn.cursor()
        cursor.execute(statement, data)
        result = cursor.fetchall()
        cursor.close()
        cxn.close()

        return result


    def insertUser(self, email, password, first_name, last_name):
        user_insert = ("INSERT INTO user "
                    "(email, password, first_name, last_name) "
                    "VALUES (%s, %s, %s, %s) ;")
        user_data = (email, password, first_name, last_name)

        self._DB_CUD(user_insert, user_data)

    
    def removeUser(self, email, password):
        user_remove = ("DELETE FROM user "
                        "WHERE email = %s AND password = %s ;")

        self._DB_CUD(user_remove, (email, password))


    def selectUser(self, email):
        user_query = ("SELECT first_name, last_name FROM user "
                        "WHERE email = %s ;")
        
        return self._DB_R(user_query, (email,))


    def selectAllUsers(self):
        user_query = ("SELECT * FROM user ;")

        return self._DB_R(user_query, None)
        

    def insertPortfolio(self, name, email):
        portfolio_insert = ("INSERT INTO portfolio "
                            "(name, activation_date, user_id) SELECT %s, %s, user.id "
                            "FROM user WHERE email = %s ;")

        self._DB_CUD(portfolio_insert, (name, datetime.today(), email))

    
    def removePortfolio(self, name, email):
        portfolio_remove = ("DELETE portfolio FROM portfolio "
                                "INNER JOIN user ON portfolio.user_id = user.id "
                                "WHERE portfolio.name = %s AND user.email = %s ;")

        self._DB_CUD(portfolio_remove, (name, email))


    def selectPortfolio(self, name, email):
        portfolio_query = ("SELECT activation_date, total_value, balance FROM portfolio "
                        "INNER JOIN user ON portfolio.user_id = user.id "
                        "WHERE portfolio.name = %s AND user.email = %s ;")
        
        return self._DB_R(portfolio_query, (name, email))


    def selectAllUserPortfolios(self, email):
        portfolio_query = ("SELECT name, activation_date, total_value, balance FROM portfolio "
                        "INNER JOIN user ON portfolio.user_id = user.id "
                        "WHERE user.email = %s ;")
        
        return self._DB_R(portfolio_query, (email,))


    def selectAllPortfolios(self):
        portfolio_query = ("SELECT * FROM portfolio ;")

        return self._DB_R(portfolio_query, None)


    def insertStock(self, ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low):
        stock_insert = ("INSERT INTO stock "
                    "(ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ;")
        stock_data = (ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low)

        self._DB_CUD(stock_insert, stock_data)


    def removeStock(self, ticker):
        stock_remove = ("DELETE FROM stock "
                        "WHERE ticker = %s ;")

        self._DB_CUD(stock_remove, (ticker, ))
        
    
    def selectStock(self, ticker):
        stock_query = ("SELECT name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low "
                        "FROM stock WHERE ticker = %s ;")

        return self._DB_R(stock_query, (ticker,))


    def selectAllStocks(self):
        stock_query = ("SELECT * FROM stock ;")

        return self._DB_R(stock_query, None)


    def purchaseStock(self, shares, ticker, email, portfolio_name):
        purchase_insert = ("INSERT INTO stock_portfolio (shares, purchase_price, purchase_date, portfolio_id, stock_ticker) "
                            "SELECT %s, stock.current_price, %s, portfolio.id, stock.ticker "
                            "FROM stock, portfolio INNER JOIN user WHERE portfolio.user_id = user.id "
                            "AND stock.ticker = %s AND user.email = %s AND portfolio.name = %s ;")
        purchase_data = (shares, datetime.today(), ticker, email, portfolio_name)

        #Manage update of portfolio value and balance here

        self._DB_CUD(purchase_insert, purchase_data)


    def sellStock(self, ticker, email, portfolio_name):
        sell_remove = ("DELETE stock_portfolio FROM stock_portfolio "
                        "INNER JOIN portfolio ON stock_portfolio.portfolio_id = portfolio.id "
                        "INNER JOIN user ON portfolio.user_id = user.id "
                        "WHERE stock_portfolio.stock_ticker = %s "
                        "AND user.email = %s AND portfolio.name = %s ;")

        #Manage update of portfolio value and balance here
        
        self._DB_R(sell_remove, (ticker, email, portfolio_name))


    def selectPortfolioStocks(self, email, portfolio_name):
        purchase_query = ("SELECT shares, purchase_price, purchase_date "
                            "FROM stock_portfolio "
                            "INNER JOIN portfolio ON stock_portfolio.portfolio_id = portfolio.id "
                            "INNER JOIN user ON portfolio.user_id = user.id "
                            "WHERE user.email = %s AND portfolio.name = %s ;")
        
        return self._DB_R(purchase_query, (email, portfolio_name))


    def selectAllPurchasedStock(self):
        purchase_query = ("SELECT * from stock_portfolio ;")

        return self._DB_R(purchase_query, None)


    def insertStockHistory(self, ticker, date, price, quantity):
        history_insert = ("INSERT INTO stock_history (ticker, date, price, quantity) "
                            "VALUES (%s, %s, %s, %s) ;")

        self._DB_CUD(history_insert, (ticker, date, price, quantity))


    def removeStockHisotry(self, ticker):
        history_remove = ("DELETE FROM stock_history WHERE ticker = %s ;")

        self._DB_CUD(history_remove, (ticker,))


    def selectStockHistory(self, ticker):
        history_query = ("SELECT * FROM stock_history "
                            "WHERE ticker = %s ;")\

        return self._DB_R(history_query, (ticker,))


    def selectAllStockHistories(self):
        history_query = ("SELECT * FROM stock_history ;")

        return self._DB_R(history_query, None)
 

    def insertStockWatch(self, email, ticker):
        watch_insert = ("INSERT INTO watchlist (user_id, stock_ticker) "
                            "SELECT user.id, %s FROM user WHERE user.email = %s ;")

        # If added to watchlist then we'll need to add to stock and stock_history most likely.
        # Should happen in flask. Use API to get info, call insert to all 3.

        self._DB_CUD(watch_insert, (ticker, email))


    def removeStockWatch(self, email, ticker):
        watch_remove = ("DELETE watchlist FROM watchlist "
                            "INNER JOIN user ON watchlist.user_id = user.id "
                            "WHERE user.email = %s AND watchlist.stock_ticker = %s ;")

        self._DB_CUD(watch_remove, (email, ticker))


    def selectUserWatchlist(self, email):
        watch_query = ("SELECT stock_ticker FROM watchlist "
                        "INNER JOIN user ON watchlist.user_id = user.id "
                        "WHERE user.email = %s ;")

        # Edit query to inner join stock and return more than just ticker name for front end convenience.
        
        return self._DB_R(watch_query, (email,))


    def selectAllWatchedStock(self):
        watch_query = ("SELECT * FROM watchlist ;")

        return self._DB_R(watch_query, None)

minion = DBminion('derringa', 'america', '10.0.0.183', 'stock_app')

# minion.insertUser('andy@gmail.com', 'america', 'Andy', 'Derringer')
# minion.insertPortfolio('new', 'andy@gmail.com')
# minion.insertStock("AMZN", "Amazon.com Inc", "5.5", "7.79", "5", "15.44", "13.10", "4.99")
# minion.insertStock("GOOG", "Alphabet Inc", "5.5", "7.79", "5", "15.44", "13.10", "4.99")
# minion.insertStock("COST", "Costco Wholesale Inc", "5.5", "7.79", "5", "15.44", "13.10", "4.99")
# minion.purchaseStock(5, 'GOOG', 'andy@gmail.com', 'new')
# minion.purchaseStock(10, 'AMZN', 'andy@gmail.com', 'new')
# minion.purchaseStock(15, 'COST', 'andy@gmail.com', 'new')

# print(minion.selectAllStocks())
# print(minion.selectAllPortfolios())
# print(minion.selectAllUsers())
# print(minion.selectAllPurchasedStock())

# minion.insertStockWatch('andy@gmail.com', 'COST')
# minion.insertStockWatch('andy@gmail.com', 'AMZN')
# minion.removeStockWatch('andy@gmail.com', 'GOOG')
# print(minion.selectAllWatchedStock())
# print(minion.selectUserWatchlist('andy@gmail.com'))

# minion.insertStockHistory('AMZN', datetime.today(), 76.22, 45)
print(minion.selectAllStockHistories())
minion.removeStockHisotry('GOOG')
print(minion.selectAllStockHistories())