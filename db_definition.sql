DROP TABLE IF EXISTS `stock`;
DROP TABLE IF EXISTS `watchlist_stock`;
DROP TABLE IF EXISTS `watchlist`;
DROP TABLE IF EXISTS `portfolio`;
DROP TABLE IF EXISTS `portfolio_stock`;
DROP TABLE IF EXISTS `user`;

CREATE TABLE user (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(254) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	balance FLOAT DEFAULT 0
);
 
CREATE TABLE portfolio (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
	activation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	total_value FLOAT DEFAULT 0 NOT NULL,
	user_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE stock (
	ticker VARCHAR(255) PRIMARY KEY NOT NULL,
	name VARCHAR(255) NOT NULL,
	current_price FLOAT NOT NULL // Need for this depends on our use of API
);

CREATE TABLE stock_portfolio (
    quantity INT NOT NULL,
	purchase_price FLOAT NOT NULL,
   	purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP,
   	portfolio_id INT NOT NULL,
	stock_ticker VARCHAR(255) NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(id),
	FOREIGN KEY (stock_ticker) REFERENCES stock(ticker)
);

-- Current Issue: Does a user have one watchlist that they add stocks to OR 
-- Is a watchlist essentially a faux portfolio and the user can have many watchlists

CREATE TABLE watchlist (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
	user_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE watchlist_stock (
	id INT AUTO_INCREMENT PRIMARY KEY,
	watchlist_id INT NOT NULL,
    stock_ticker VARCHAR(255) NOT NULL,
	FOREIGN KEY (watchlist_id) REFERENCES watchlist(id),
    FOREIGN KEY (stock_ticker) REFERENCES stock(ticker)
);
