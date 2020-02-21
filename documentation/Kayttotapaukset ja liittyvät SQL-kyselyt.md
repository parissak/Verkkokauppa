# Käyttötapaukset

* Käyttäjänä voin rekisteröityä sivustolle.

`INSERT INTO account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)`

* Käyttäjänä voin rekisteröityä sivustolle.

`SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account WHERE account.id = ?`

* Käyttäjänä voin tarkastella myynnissä olevia tuotteita.

`SELECT * FROM product JOIN Account ON Account.id = Account_id JOIN Category ON Category.id = Category_id;`

* Käyttäjänä voin hakea tuotteita. 

`SELECT product.id AS product_id, product.date_created AS product_date_created, product.date_modified AS product_date_modified, product.name AS product_name, product.price AS product_price, product.description AS product_description, product.account_id AS product_account_id, product.category_id AS product_category_id 
FROM product WHERE product.name = ?`


 <br/><br/>
 
* Rekisteröityneenä käyttäjänä voin lisätä tuotteita sivustolle.

`INSERT INTO Product ('name', 'price', 'description', 'account_id', 'category_id') VALUES (?, ?, ?, ?, ?);`

* Rekisteröityneenä käyttäjänä voin poistaa lisäämäni tuotteen sivustolta. 

`DELETE FROM Product WHERE product.id = ?;`

* Rekisteröityneenä käyttäjänä voin muuttaa tuotteeni kuvausta.

`UPDATE Product SET Description = ? WHERE product.id = ?;`

* Rekisteröityneenä käyttäjänä voin tarkastella profiiliani ja lisäämiäni tuotteita.

`SELECT * FROM product JOIN Account ON Account.id = Account_id JOIN Category ON Category.id = Category_id WHERE Account.id = ?;`


* Rekisteröityneenä käyttäjänä voin ostaa tai tilata tuotteen alustan kautta.
``
