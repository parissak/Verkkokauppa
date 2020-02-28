CREATE TABLE User (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE Product (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	name VARCHAR(144) NOT NULL, 
	price FLOAT NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	user_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);

CREATE TABLE Order (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	user_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);

CREATE TABLE Category (
	id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id)
);
