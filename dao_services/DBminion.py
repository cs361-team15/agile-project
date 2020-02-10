import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


class DBminion:

    def __init__(self, u, p, h, db, parent=None):

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


    def add_user(self, email, password, first_name, last_name):
        user_insert = ("INSERT INTO user "
                    "(email, password, first_name, last_name) "
                    "VALUES (%s, %s, %s, %s) ;")
        user_data = (email, password, first_name, last_name)

        self._DB_CUD(user_insert, user_data)

    
    def remove_user(self, email, password):
        user_remove = ("DELETE FROM user "
                        "WHERE email = %s AND password = %s ;")

        self._DB_CUD(user_remove, (email, password))


    def get_user(self, email):
        user_query = ("SELECT first_name, last_name FROM user "
                        "WHERE email = %s ;")
        
        return self._DB_R(user_query, (email,))


    def get_all_users(self):
        user_query = ("SELECT * FROM user ;")

        return self._DB_R(user_query, None)
        

    def add_portfolio(self, name, email):
        #activation_date = datetime.today().strftime('%Y-%m-%d')
        #print(activation_date)
        portfolio_insert = ("INSERT INTO portfolio "
                            "(name, activation_date, user_id) SELECT %s, %s, user.id "
                            "FROM user WHERE email = %s ;")

        self._DB_CUD(portfolio_insert, (name, datetime.today(), email))

    
    # def remove_portfolio(self, name, email):
    #     portfolio_remove = ("DELETE")

    def get_all_portfolios(self):
        portfolio_query = ("SELECT * FROM portfolio ;")

        return self._DB_R(portfolio_query, None)





minion = DBminion('derringa', 'america', '10.0.0.183', 'stock_app')
minion.add_portfolio("sports", 'robert@gmail.com')
print(minion.get_all_portfolios())
