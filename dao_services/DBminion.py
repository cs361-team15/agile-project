import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


class DBminion:

    def __init__(self, u, pw, h, prt, db):

        self.DBconfig = {
            'user': u,
            'password': pw,
            'host': h,
            'port': prt,
            'database': db
        }


    def _DB_cxn(self):
        '''
        Summary:    Modularized mysql connection creator using database credentials
                    stored in DBminion class variables.
        Params:     None.
        Outputs:    [1] mysql connection object.
        '''
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
        '''
        Summary:    Modularized database connection and cursor commands for
                    insert, update, and delete commands.
        Params:     [1] SQL statement string.
                    [2] Tuple of variables for insertion in statement string.
        Outputs:    None.
        '''
        cxn = self._DB_cxn()
        cursor = cxn.cursor()
        cursor.execute(statement, data)
        cxn.commit()
        cursor.close()
        cxn.close()

    
    def _DB_R(self, statement, data):
        '''
        Summary:    Modularized database connection and cursor commands for selection.
        Params:     [1] SQL statement string.
                    [2] Tuple of variables for insertion in statement string.
        Outputs:    [1] List of dictionaries for each selection query return.
        '''
        cxn = self._DB_cxn()
        cursor = cxn.cursor(dictionary=True)
        cursor.execute(statement, data)
        result = cursor.fetchall()
        cursor.close()
        cxn.close()

        return result


    def insertUser(self, email, password, first_name, last_name):
        '''
        Summary:    Insert new user into user table.
        Params:     [1] user email string.
                    [2] user password string.
                    [3] user first name string.
                    [4] user last name string.
        Outputs:    None.
        '''
        user_insert = ("INSERT INTO user "
                    "(email, password, first_name, last_name) "
                    "VALUES (%s, %s, %s, %s) ;")
        user_data = (email, password, first_name, last_name)

        self._DB_CUD(user_insert, user_data)

    
    def removeUser(self, email, password):
        '''
        Summary:    Removes user if correction email and password credentials.
        Params:     [1] user email string.
                    [2] user password string.
        Outputs:    None.
        '''
        user_remove = ("DELETE FROM user "
                        "WHERE email = %s AND password = %s ;")

        self._DB_CUD(user_remove, (email, password))


    def selectUser(self, email):
        '''
        Summary:    Returns user of unique email attribute value.
        Params:     [1] user email string.
        Outputs:    [1] list of dictionary for user matching unique criteria.
        '''
        user_query = ("SELECT first_name, last_name FROM user "
                        "WHERE email = %s ;")
        
        return self._DB_R(user_query, (email,))


    def selectAllUsers(self):
        '''
        Summary:    Return all users in the database.
        Params:     None.
        Outputs:    List of dictionaries of all users.
        '''
        user_query = ("SELECT * FROM user ;")

        return self._DB_R(user_query, None)
        

    def insertPortfolio(self, portfolio_name, email):
        '''
        Summary:    Insert portfolio into database by unique combined values of
                    portfolio name and user email.
        Params:     [1] portfolio name string.
                    [2] user email string.
        Outputs:    None.
        '''
        portfolio_insert = ("INSERT INTO portfolio "
                            "(name, activation_date, user_id) SELECT %s, %s, user.id "
                            "FROM user WHERE email = %s ;")

        self._DB_CUD(portfolio_insert, (portfolio_name, datetime.today(), email))

    
    def removePortfolio(self, portfolio_name, email):
        '''
        Summary:    Remove user portfolio of particular name from database.
        Params:     [1] portfolio name string.
                    [2] user email string.
        Outputs:    None.
        '''
        portfolio_remove = ("DELETE portfolio FROM portfolio "
                                "INNER JOIN user ON portfolio.user_id = user.id "
                                "WHERE portfolio.name = %s AND user.email = %s ;")

        self._DB_CUD(portfolio_remove, (portfolio_name, email))


    def addPortfolioBalance(self, transfer, email, portfolio_name):
        '''
        Summary:    Increases balance and thus total value of a portfolio.
        Params:     [1] money transfer amount integer.
                    [2] user email string.
                    [3] portfolio name string.
        Outputs:    None.
        '''
        portfolio_update = ("UPDATE portfolio INNER JOIN user ON portfolio.user_id = user.id "
                            "SET balance = balance + %s, total_value = total_value + %s "
                            "WHERE user.email = %s AND portfolio.name = %s ;")

        self._DB_CUD(portfolio_update, (transfer, transfer, email, portfolio_name))


    def _updatePortfolioBalance(self, shares, stock_value, email, portfolio_name):
        '''
        Summary:    Called by purchaseStock() and sellStock(). Increases or decreases the
                    balance of a portfolio by shares moved and their value.
        Params:     [1] stock shares integer.
                    [2] stock value integer.
                    [3] user email string.
                    [4] portfolio name string.
        Outputs:    None.
        '''
        portfolio_update = ("UPDATE portfolio INNER JOIN user ON portfolio.user_id = user.id "
                            "SET balance = balance + %s "
                            "WHERE user.email = %s AND portfolio.name = %s ;")
        
        self._DB_CUD(portfolio_update, ((shares * stock_value), email, portfolio_name))


    def selectPortfolio(self, portfolio_name, email):
        '''
        Summary:    Returns portfolio of a particular name belonging to a particular user.
        Params:     [1] portfolio name string.
                    [2] user email string.
        Outputs:    [1] list of dictionary for single portfolio return.
        '''
        portfolio_query = ("SELECT activation_date, total_value, balance FROM portfolio "
                        "INNER JOIN user ON portfolio.user_id = user.id "
                        "WHERE portfolio.name = %s AND user.email = %s ;")
        
        return self._DB_R(portfolio_query, (portfolio_name, email))


    def selectAllUserPortfolios(self, email):
        '''
        Summary:    Return all portfolios belonging to a particular user.
        Params:     [1] user email string.
        Outputs:    [1] list of dictionaries for all portfolios meeting criteria.
        '''
        portfolio_query = ("SELECT name, activation_date, total_value, balance FROM portfolio "
                        "INNER JOIN user ON portfolio.user_id = user.id "
                        "WHERE user.email = %s ;")
        
        return self._DB_R(portfolio_query, (email,))


    def selectAllPortfolios(self):
        '''
        Summary:    Returns all entities in the database portfolio table.
        Params:     None.
        Outputs:    [1] List of dictionaries for every portfolio.
        '''
        portfolio_query = ("SELECT * FROM portfolio ;")

        return self._DB_R(portfolio_query, None)


    def insertUpdateStock(self, ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low):
        '''
        Summary:    Inserts new stock unless duplicate ticker value exists then updates other attribute values.
        Params:     [1] stock ticker string.
                    [2] stock name string.
                    [3] stock opening price float.
                    [4] stock current price float.
                    [5] stock market cap float.
                    [6] stock 52 week high float.
                    [7] stock 52 week low float.
        Outputs:    None.
        '''
        stock_insert = ("INSERT INTO stock "
                    "(ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
                    "ON DUPLICATE KEY UPDATE open_price = values(open_price), current_price = values(current_price), "
                    "current_volume = values(current_volume), market_cap = values(market_cap), "
                    "fifty_two_week_high = values(fifty_two_week_high), fifty_two_week_low = values(fifty_two_week_low) ;")
        stock_data = (ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low)

        self._DB_CUD(stock_insert, stock_data)


    def removeStock(self, ticker):
        '''
        Summary:    Removes stock of particular ticker from database.
        Params:     [1] stock ticker string.
        Outputs:    None.
        '''
        stock_remove = ("DELETE FROM stock "
                        "WHERE ticker = %s ;")

        self._DB_CUD(stock_remove, (ticker, ))
        
    
    def selectStock(self, ticker):
        '''
        Summary:    Returns stock of particular ticker value.
        Params:     [1] stock ticker string.
        Outputs:    [1] list of dictionary for unique stock entity returned.
        '''
        stock_query = ("SELECT name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low "
                        "FROM stock WHERE ticker = %s ;")

        return self._DB_R(stock_query, (ticker,))


    def selectAllStocks(self):
        '''
        Summary:    Returns all entities in the database table.
        Params:     None.
        Outputs:    [1] list of dictionaries for each entity returned.
        '''
        stock_query = ("SELECT * FROM stock ;")

        return self._DB_R(stock_query, None)


    def purchaseStock(self, shares, ticker, email, portfolio_name):
        '''
        Summary:    Inserts new stock entity or updates existing depending on if matching
                    combination of ticker, email, portfolio, and purchase price already present.
        Params:     [1] stock shares integer.
                    [2] stock ticker string.
                    [3] user email string.
                    [4] portfolio name string.
        Outputs:    None.
        '''

        # Insert stock or update on duplicate
        purchase_insert = ("INSERT INTO stock_portfolio (shares, purchase_price, purchase_date, portfolio_id, stock_ticker) "
                            "SELECT %s, stock.current_price, %s, portfolio.id, stock.ticker "
                            "FROM stock, portfolio INNER JOIN user WHERE portfolio.user_id = user.id "
                            "AND stock.ticker = %s AND user.email = %s AND portfolio.name = %s "
                            "ON DUPLICATE KEY UPDATE shares = shares + values(shares) ;")
        purchase_data = (shares, datetime.today(), ticker, email, portfolio_name)

        # Retreive current price of stock being purchased from stock table.
        stock_value = self.selectStock(ticker)[0]['current_price']

        #Make statements to add stocks to portfolio and update portfolio balance.
        self._updatePortfolioBalance(shares * -1, stock_value, email, portfolio_name)
        self._DB_CUD(purchase_insert, purchase_data)


    def sellStock(self, shares, ticker, email, portfolio_name):
        '''
        Summary:    Update stock quantity after sell or if zero remaining then remove from table
                    followed by update of portfolio balance.
        Params:     [1] stock shares integer.
                    [2] stock ticker string.
                    [3] user email string.
                    [4] portfolio name string.
        Outputs:    None.
        '''

        # Get stock purchase information from portfolio in question.
        stock_purchase = self.selectIndividualPortfolioStock(ticker, email, portfolio_name)

        # Get most recently update price of stock from stock table.
        curr_price = self.selectStock(ticker)[0]['current_price']

        # Calculate number of remaining stock.
        remaining_stock = stock_purchase[0]['shares'] - shares

        if remaining_stock <= 0: #If remaining is 0 delete entity.
            remaining_stock = stock
            sell_remove = ("DELETE stock_portfolio FROM stock_portfolio "
                            "INNER JOIN portfolio ON stock_portfolio.portfolio_id = portfolio.id "
                            "INNER JOIN user ON portfolio.user_id = user.id "
                            "WHERE stock_portfolio.stock_ticker = %s "
                            "AND user.email = %s AND portfolio.name = %s ;")
            self._DB_CUD(sell_remove, (ticker, email, portfolio_name))
        else: #Else update share quantity.
            sell_update = ("UPDATE stock_portfolio INNER JOIN portfolio ON stock_portfolio.portfolio_id = portfolio.id "
                            "INNER JOIN user ON portfolio.user_id = user.id "
                            "SET shares = shares - %s "
                            "WHERE stock_portfolio.stock_ticker = %s AND user.email = %s AND portfolio.name = %s ;")
            self._DB_CUD(sell_update, (shares, ticker, email, portfolio_name))
        
        # Update portfolio balance.
        self._updatePortfolioBalance(shares, curr_price, email, portfolio_name)
        

    def selectPortfolioStocks(self, email, portfolio_name):
        '''
        Summary:    Return stocks of a particular user and portfolio.
        Params:     [1] user email string.
                    [2] portfolio name string.
        Outputs:    [1] list of dictionaries for each stock entity in that user portfolio.
        '''
        purchase_query = ("SELECT stock_ticker, shares, purchase_price, purchase_date "
                            "FROM stock_portfolio "
                            "INNER JOIN portfolio ON stock_portfolio.portfolio_id = portfolio.id "
                            "INNER JOIN user ON portfolio.user_id = user.id "
                            "WHERE user.email = %s AND portfolio.name = %s ;")
        
        return self._DB_R(purchase_query, (email, portfolio_name))


    def selectIndividualPortfolioStock(self, ticker, email, portfolio_name):
        '''
        Summary:    Returns an individual stock purchased at different times and values within 
                    a particular user portfolio.
        Params:     [1] stock ticker string.
                    [2] user email string.
                    [3] portfolio name string.
        Outputs:    [1] list of dictionaries for unique stock bought at varies times and values.
        '''
        purchase_query = ("SELECT stock_ticker, shares, purchase_price, purchase_date "
                            "FROM stock_portfolio "
                            "INNER JOIN portfolio ON stock_portfolio.portfolio_id = portfolio.id "
                            "INNER JOIN user ON portfolio.user_id = user.id "
                            "WHERE stock_ticker = %s AND user.email = %s AND portfolio.name = %s ;")

        return self._DB_R(purchase_query, (ticker, email, portfolio_name))


    def selectAllPurchasedStock(self):
        '''
        Summary:    Return all purchased stocked contained in any portfolio within the database.
        Params:     None.
        Outputs:    [1] list of dictionaries for each unique stock portfolio purchase entity.
        '''
        purchase_query = ("SELECT * from stock_portfolio ;")

        return self._DB_R(purchase_query, None)


    def insertStockHistory(self, ticker, date, price, quantity):
        '''
        Summary:    Insert stock price and quantity history at a particular date.
        Params:     [1] stock ticker string.
                    [2] date 'yyyy-mm-dd'.
                    [3] stock price float.
                    [4] stock quantity integer.
        Outputs:    None.
        '''
        history_insert = ("INSERT INTO stock_history (ticker, date, price, quantity) "
                            "VALUES (%s, %s, %s, %s) ;")

        self._DB_CUD(history_insert, (ticker, date, price, quantity))


    def removeStockHisotry(self, ticker):
        '''
        Summary:    Deletes all history for a particular stock by ticker.
        Params:     [1] stock ticker string.
        Outputs:    None.
        '''
        history_remove = ("DELETE FROM stock_history WHERE ticker = %s ;")

        self._DB_CUD(history_remove, (ticker,))


    def selectStockHistory(self, ticker):
        '''
        Summary:    Returns every date entry for a particular stock value within stock history table.
        Params:     [1] stock ticker string.
        Outputs:    [1] List of dictionaries for every date entiry of a particular stock ticker.
        '''
        history_query = ("SELECT * FROM stock_history "
                            "WHERE ticker = %s ;")\

        return self._DB_R(history_query, (ticker,))


    def selectAllStockHistories(self):
        '''
        Summary:    Returns all entities for each stock at every date in the table.
        Params:     None.
        Outputs:    [1] List of dictionaries for each entity in the stock history table.
        '''
        history_query = ("SELECT * FROM stock_history ;")

        return self._DB_R(history_query, None)
 

    def insertStockWatch(self, email, ticker):
        '''
        Summary:    Inserts stock ticker into watchlist for a particular user.
        Params:     [1] user email string.
                    [2] stock ticker string.
        Outputs:    None.
        '''
        watch_insert = ("INSERT INTO watchlist (user_id, stock_ticker) "
                            "SELECT user.id, %s FROM user WHERE user.email = %s ;")

        # If added to watchlist then we'll need to add to stock and stock_history most likely.
        # Should happen in flask. Use API to get info, call insert to all 3.

        self._DB_CUD(watch_insert, (ticker, email))


    def removeStockWatch(self, email, ticker):
        '''
        Summary:    Removes particular stock from watchlist of specified user.
        Params:     [1] user email string.
                    [2] stock ticker string.
        Outputs:    None.
        '''
        watch_remove = ("DELETE watchlist FROM watchlist "
                            "INNER JOIN user ON watchlist.user_id = user.id "
                            "WHERE user.email = %s AND watchlist.stock_ticker = %s ;")

        self._DB_CUD(watch_remove, (email, ticker))


    def selectUserWatchlist(self, email):
        '''
        Summary:    Returns all stocks currently being watched by a particular user.
        Params:     [1] user email string.
        Outputs:    [1] list of dictionaries for each entity on user watchlist.
        '''
        watch_query = ("SELECT stock_ticker FROM watchlist "
                        "INNER JOIN user ON watchlist.user_id = user.id "
                        "WHERE user.email = %s ;")

        # Edit query to inner join stock and return more than just ticker name for front end convenience.
        
        return self._DB_R(watch_query, (email,))


    def selectAllWatchedStock(self):
        '''
        Summary:    Return all watched stocks on every user watchlist.
        Params:     None.
        Outputs:    [1] list of dictionaries for each entity on all watchlists.
        '''
        watch_query = ("SELECT * FROM watchlist ;")

        return self._DB_R(watch_query, None)

minion = DBminion('group_fifteen', 'oregonstate', 'stocks-db.cyuqmchnvglv.us-east-2.rds.amazonaws.com', '3306', 'stock-app')

# minion.insertUser('andy@gmail.com', 'germany', 'Andy', 'Derringer')

for user in minion.selectAllUsers():
    print(user)