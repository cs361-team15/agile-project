# project/app.py
from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity
from services.ApplicationService import ApplicationService
from services.DaoService import DaoService

app = Flask(__name__)

minion = DaoService('group_fifteen', 'oregonstate', 'stocks-db.cyuqmchnvglv.us-east-2.rds.amazonaws.com', '3306', 'stock-app')
appService = ApplicationService(minion)

# test route
@app.route('/')
def foobar():
    return ', '.join([user['first_name'] for user in minion.selectAllUsers()])

############            ############
############ Auth   API ############
############            ############

# def authenticate(email, password):
#     user = minion.selectUser(email)
#     if user['email'] == email and user['password'] == password:
#         return user

# def identity(userPayload):
#     user_id = userPayload['user_id']
#     return user_id

# jwt = JWT(app, authenticate, identity)

# #Send a post request with {'username': , 'password': }
# #Returns an 'access_token'
# @app.route('/protected')
# @jwt_required()
# def protected():
#     return '%s' % current_identity


############            ############
############ Actual API ############
############            ############

@app.route('/authentication', methods=['POST'])
def authentication():
    email = request.json['email']
    password = request.json['password']
    user = minion.selectUser(email)
    userDict = user[0]
    if userDict.get('password') == password:
        return "Email and Password Ok"
    else:
        return "Bad Email Password"


@app.route('/user', methods=['POST','GET','PUT'])
def user():
    if request.method == 'POST' and request.json:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        password = request.json['password']
        minion.insertUser(email, password, first_name, last_name)
        return 'POST request successful'
    elif request.method == 'GET':
        email = request.args.get('email')
        user = minion.selectUser(email)
        return jsonify(user)
    elif request.method == 'PUT' and request.json:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        password = request.json['password']
        #needs user update DAO
    return 'failure'

@app.route('/portfolios', methods=['POST','GET','PUT','DELETE'])
def portfolios():
    if request.method == 'GET':
        portfolios = minion.selectAllPortfolios()
        return jsonify(portfolios)


# ############		  ############
# ############ USER API ############
# ############		  ############

'''
      Summary:    Insert new user into user table.
      Params:     POST Request
            'first_name': 
                  'last_name': 
                  'email': 
                  'password': 
      Outputs:    None.
'''
@app.route('/insertUser', methods=['POST','GET'])
def insertUser():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    minion.insertUser(email, password, first_name, last_name)
    #Should return a way to note it was successful/unsuccesful?


'''
      Summary:    Remove a user from user tables
      Params:     POST Request
                  'email': 
                  'password': 
      Outputs:    None.
'''
@app.route('/removeUser', methods=['POST','GET'])
def removeUser():
    email = request.json['email']
    password = request.json['password']
    minion.removeUser(email, password)

'''
      Summary:    Select a specific user by email
      Params:     POST Request
                  'email': 
      Outputs:    Dict of first name and last name of user
'''
@app.route('/selectUser', methods=['POST','GET'])
def selectUser():
    email = request.json['email']
    user = minion.selectUser(email)
    return jsonify(user)

'''
      Summary:    Get a list of all users
      Params:     POST Request
      Outputs:    Dict of all users
'''
@app.route('/selectAllUsers', methods=['POST','GET'])
def selectAllUsers():
    userList = minion.selectAllUsers()
    return jsonify(userList)

############		       #############
############ PORTFOLIO API #############
############		       #############


'''
      Summary:    Insert portfolio into database by unique combined values of
                  portfolio name and user email.
      Params:     POST Request
                  'email': 
                  'portfolio': portfolio name
      Outputs:    None.
'''
@app.route('/insertPortfolio', methods=['POST','GET'])
def insertPortfolio():
    email = request.json['email']
    portfolio = request.json['portfolio']
    minion.insertPortfolio(portfolio, email)

'''
      Summary:    Remove portfolio of specific name from a user
      Params:     POST Request
                  'email': 
                  'portfolio': portfolio name
      Outputs:    None.
'''
@app.route('/removePortfolio', methods=['POST','GET'])
def removePortfolio():
    email = request.json['email']
    portfolio = request.json['portfolio']
    minion.removePortfolio(portfolio, email)

'''
      Summary:    Add to the balance of a portfolio
      Params:     POST Request
            'transfer': 
                  'email': 
                  'portfolio': portfolio name
      Outputs:    None.
'''
@app.route('/addPortfolioBalance', methods=['POST','GET'])
def addPortfolioBalance():
    transfer = request.json['transfer']
    email = request.json['email']
    portfolio = request.json['portfolio']
    minion.addPortfolioBalance(transfer, email, portfolio) #In the DB_CUD_ there was two trasnfer args?

'''
      Summary:    Select a portfolio by name of a user
      Params:     POST Request
            'email': 
                  'portfolio': 
      Outputs:    Dict of a portfolio
'''
@app.route('/selectPortfolio', methods=['POST','GET'])
def selectPortfolio():
    email = request.json['email']
    portfolio = request.json['portfolio']
    onePortfolio = minion.selectPortfolio(portfolio, email)
    return jsonify(onePortfolio)

'''
      Summary:    Select all portfolios of a user
      Params:     POST Request
                  'email': 
      Outputs:    Dict of all portfolios of a user.
'''
@app.route('/selectAllUserPortfolios', methods=['POST','GET'])
def selectAllUserPortfolios():
    email = request.json['email']
    portfolios = minion.selectAllUserPortfolios(email)
    return jsonify(portfolios)

'''
      Summary:    Select all portfolios of all users
      Params:     POST Request
      Outputs:    Dict of all portfolios
'''
@app.route('/selectAllPortfolios', methods=['POST','GET'])
def selectAllPortfolios():
    onePortfolio = minion.selectAllPortfolios()
    return jsonify(onePortfolio)

############		   #############
############ STOCK API #############
############		   #############


'''
      Summary:    Inserts new stock unless duplicate ticker value exists then updates other attribute values
      Params:     POST Request
            'ticker': 
                  'name': 
                  'open_price': 
                  'current_price': 
            'current_volume': 
                  'market_cap': 
                  'fifty_two_week_high': 
                  'fifty_two_week_low': 
      Outputs:    None.
'''
@app.route('/insertUpdateStock', methods=['POST','GET'])
def insertUpdateStock():
    ticker = request.json['ticker']
    name = request.json['name']
    open_price = request.json['open_price']
    current_price = request.json['current_price']
    current_volume = request.json['current_volume']
    market_cap = request.json['market_cap']
    fifty_two_week_high = request.json['fifty_two_week_high']
    fifty_two_week_low = request.json['fifty_two_week_low']
    minion.insertUpdateStock(ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low)

'''
      Summary:    Removes stock of particular ticker from database
      Params:     POST Request
            'ticker': 
      Outputs:    None.
'''
@app.route('/removeStock', methods=['POST','GET'])
def removeStock():
    ticker = request.json['ticker']
    minion.removeStock(ticker)

'''
      Summary:    Returns stock of particular ticker value.
      Params:     POST Request
            'ticker': 
      Outputs:    dict for unique stock entity.
'''
@app.route('/selectStock', methods=['POST','GET'])
def selectStock():
    ticker = request.json['ticker']
    stock = minion.selectStock(ticker)
    return stock

'''
      Summary:    Returns all entities in the database table.
      Params:     POST Request
      Outputs:    Dict of all stocks.
'''
@app.route('/selectAllStocks', methods=['POST','GET'])
def selectAllStocks():
    stocks = minion.selectAllStocks()
    return stocks

'''
      Summary:    Inserts new stock entity or updates existing depending on if matching
                  combination of ticker, email, portfolio, and purchase price already present
      Params:     POST Request
                  'shares': 
                  'ticker': 
                  'email': 
                  'portfolio': 
      Outputs:    None.
'''
@app.route('/purchaseStock', methods=['POST','GET'])
def purchaseStock():
    shares = request.json['shares']
    ticker = request.json['ticker']
    email = request.json['email']
    portfolio = request.json['portfolio']
    minion.purchaseStock(shares, ticker, email, portfolio)

'''
      Summary:    Sells stock shares 
      Params:     POST Request
                  'shares': 
                  'ticker': 
                  'email': 
                  'portfolio': 
      Outputs:    None.
'''
@app.route('/sellStock', methods=['POST','GET'])
def sellStock():
    shares = request.json['shares']
    ticker = request.json['ticker']
    email = request.json['email']
    portfolio = request.json['portfolio']
    minion.sellStock(shares, ticker, email, portfolio)

'''
      Summary:    Return stocks of a particular user and portfolio.
      Params:     POST Request
                  'email': 
                  'portfolio': 
      Outputs:    None.
'''
@app.route('/selectPortfolioStocks', methods=['POST','GET'])
def selectPortfolioStocks():
    email = request.json['email']
    portfolio = request.json['portfolio']
    stocks = minion.selectPortfolioStocks(email, portfolio)
    return stocks

'''
      Summary:    Returns an individual stock purchased at different times and values within 
                  a particular user portfolio.
      Params:     POST Request
                  'ticker': 
                  'email': 
                  'portfolio': 
      Outputs:    None.
'''
@app.route('/selectIndividualPortfolioStock', methods=['POST','GET'])
def selectIndividualPortfolioStock():
    ticker = request.json['ticker']
    email = request.json['email']
    portfolio = request.json['portfolio']
    stock = minion.selectIndividualPortfolioStock(ticker, email, portfolio)
    return stock

'''
      Summary:    Return all purchased stocked contained in any portfolio within the database.
      Params:     POST Request
      Outputs:    list of dictionaries for each unique stock portfolio purchase entity
'''
@app.route('/selectAllPurchasedStock', methods=['POST','GET'])
def selectAllPurchasedStock():
    stocks = minion.selectAllPurchasedStock()
    return stocks

'''
      Summary:    Insert stock price and quantity history at a particular date.
      Params:     POST Request
                  'ticker': 
                  'date': 
                  'price': 
                  'quantity': 
      Outputs:    None.
'''
@app.route('/insertStockHistory', methods=['POST','GET'])
def insertStockHistory():
    ticker = request.json['ticker']
    date = request.json['date']
    price = request.json['price']
    quantity = request.json['quantity']
    minion.insertStockHistory(ticker, date, price, quantity)

'''
      Summary:    Deletes all history for a particular stock by ticker.
      Params:     POST Request
                  'ticker': 
      Outputs:    None.
'''
@app.route('/removeStockHistory', methods=['POST','GET']) #there is a typo in the dao for this one 'hisotry'
def removeStockHistory():
    ticker = request.json['ticker']
    minion.removeStockHistory(ticker)

'''
      Summary:    Returns every date entry for a particular stock value within stock history table.
      Params:     POST Request
                  'ticker': 
      Outputs:    None.
'''
@app.route('/selectStockHistory', methods=['POST','GET'])
def selectStockHistory():
    ticker = request.json['ticker']
    stock = minion.selectStockHistory(ticker)
    return stock

'''
      Summary:    Insert new user into user table.
      Params:     POST Request
      Outputs:    None.
'''
@app.route('/selectAllStockHistories', methods=['POST','GET'])
def selectAllStockHistories():
    stocks = minion.selectAllStockHistories(ticker)
    return stocks

'''
      Summary:    Inserts stock ticker into watchlist for a particular user, also stock and stock_history
      Params:     POST Request
                  'ticker': 
                  'quantity':
                  'date': 
                  'name': 
                  'open_price': 
                  'current_price': 
                  'current_volume': 
                  'market_cap': 
                  'fifty_two_week_high': 
                  'fifty_two_week_low': 
      Outputs:    None.
'''
@app.route('/insertStockWatch', methods=['POST','GET'])
def insertStockWatch():
    ticker = request.json['ticker']
    date = request.json['date']
    price = request.json['current_price']
    quantity = request.json['quantity']
    name = request.json['name']
    open_price = request.json['open_price']
    current_volume = request.json['current_volume']
    market_cap = request.json['market_cap']
    fifty_two_week_high = request.json['fifty_two_week_high']
    fifty_two_week_low = request.json['fifty_two_week_low']
    #Updates all 3 as per DAO, will require API call for info
    minion.insertStockWatch(email, ticker)
    minion.insertStockHistory(ticker, date, price, quantity)
    minion.insertUpdateStock(ticker, name, open_price, current_price, current_volume, market_cap, fifty_two_week_high, fifty_two_week_low)

'''
      Summary:    Removes particular stock from watchlist of specified user.
      Params:     POST Request
                  'ticker': 
                  'email': 
      Outputs:    None.
'''
@app.route('/removeStockWatch', methods=['POST','GET'])
def removeStockWatch():
    ticker = request.json['ticker']
    email = request.json['email']
    minion.removeStockWatch(email, ticker)

'''
      Summary:    Returns all stocks currently being watched by a particular user.
      Params:     POST Request
                  'email': 
      Outputs:    list of dictionaries for each entity on user watchlist
'''
@app.route('/selectUserWatchlist', methods=['POST','GET'])
def selectUserWatchlist():
    email = request.json['email']
    watchlist = minion.selectUserWatchlist(email)
    return watchlist

'''
      Summary:    Return all watched stocks on every user watchlist.
      Params:     POST Request
      Outputs:    None.
'''
@app.route('/selectAllWatchedStock', methods=['POST','GET'])
def selectAllWatchedStock():
    allWatchlist = minion.selectAllWatchedStock()
    return allWatchlist
