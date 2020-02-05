-- USER CRUD

INSERT INTO user (email, password, first_name, last_name) 
VALUES ( 'andy@gmail.com', 'go_beavs2020', 'Andy', 'Derringer' );

SELECT first_name, last_name 
FROM user 
WHERE email = 'andy@gmail.com'
AND password = 'go_beavs2020' ;

UPDATE user 
SET balance = 100 
WHERE email = 'andy@gmail.com' ;

DELETE FROM user 
WHERE email = 'andy@gmail.com' 
AND password = 'go_beavs2020' ;

-- PORTFOLIO CRUD

INSERT INTO portfolio (name, user_id) 
SELECT 'Tech Companies', user.id
FROM user
WHERE email = 'andy@gmail.com' ;

SELECT p.name, p.activation_date, p.total_value 
FROM portfolio AS p
INNER JOIN user 
ON p.user_id=user.id 
WHERE user.email = 'andy@gmail.com' ;

UPDATE portfolio 
INNER JOIN user 
ON portfolio.user_id = user.id 
SET portfolio.total_value = 1000 
WHERE user.email = 'andy@gmail.com' ;

DELETE portfolio FROM portfolio
INNER JOIN user
ON portfolio.user_id = user.id 
WHERE portfolio.name = 'Tech Companies'
AND user.email = 'andy@gmail.com' ;

-- STOCK CRUD

INSERT INTO stock (ticker, name, current_price)
VALUES ( 'GOOG', 'Alphabet Inc.', 1434.23 ) ;

SELECT name, current_price
FROM stock 
WHERE ticker = 'GOOG' ;

UPDATE stock
SET current_price = 1320.75
WHERE stock.ticker = 'GOOG' ;

DELETE FROM stock
WHERE stock.ticker = 'GOOG' ;

-- STOCK_PORTFOLIO CRUD

INSERT INTO stock_portfolio ( quantity, purchase_price, portfolio_id, stock_ticker )
SELECT 4, stock.current_price, portfolio.id, stock.ticker
FROM stock, portfolio
INNER JOIN user
WHERE portfolio.user_id = user.id 
AND stock.ticker = 'GOOG' 
AND user.email = 'Andy@gmail.com' 
AND portfolio.name = 'Tech Companies';


SELECT quantity, purchase_price, purchase_date, stock_ticker
FROM stock_portfolio AS s
INNER JOIN portfolio AS p
ON  s.portfolio_id = p.id
INNER JOIN user AS u
ON  p.user_id = u.id
WHERE u.email = 'Andy@gmail.com' 
AND p.name = 'Tech Companies';

UPDATE stock_portfolio AS s
INNER JOIN portfolio AS p
ON  s.portfolio_id = p.id
INNER JOIN user AS u
ON  p.user_id = u.id
SET s.quantity = 6
WHERE s.stock_ticker = 'GOOG'
AND u.email = 'Andy@gmail.com' 
AND p.name = 'Tech Companies' ;

DELETE stock_portfolio
FROM stock_portfolio
INNER JOIN portfolio AS p
ON  stock_portfolio.portfolio_id = p.id
INNER JOIN user AS u
ON  p.user_id = u.id
WHERE stock_portfolio.stock_ticker = 'GOOG'
AND u.email = 'Andy@gmail.com' 
AND p.name = 'Tech Companies' ;
