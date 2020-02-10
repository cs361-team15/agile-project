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
        
    
    def selectAllStocks(self):
        stock_query = ("SELECT * FROM stock ;")

        return self._DB_R(stock_query, None)


minion = DBminion('derringa', 'america', '10.0.0.183', 'stock_app')

# minion.insertStock("AMZN", "Amazon.com Inc", "5.5", "7.79", "5", "15.44", "13.10", "4.99")

print(minion.selectAllStocks())
