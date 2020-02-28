# Käyttötapaukset

* Käyttäjänä voin rekisteröityä sivustolle.

`INSERT INTO account (date_created, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);`

* Käyttäjänä tai rekisteröityneenä käyttäjänä voin tarkastella myynnissä olevia tuotteita.

`SELECT * FROM product JOIN Account ON Account.id = Account_id JOIN Category ON Category.id = Category_id ORDER BY date_created DESC LIMIT ? OFFSET ?`

* Käyttäjänä tai rekisteröityneenä käyttäjänä voin hakea tuotteita nimen perusteella. 

`SELECT * FROM product WHERE product.name = ?;`

* Käyttäjänä näen tilatuimpia tuotteita.
`Select Product.name FROM Order JOIN Product on Product.id = product_id JOIN Account ON account.id = product.account_id GROUP BY product.id ORDER BY COUNT(product.id) DESC LIMIT 3;`

 <br/><br/>
 
 * Rekisteröityneenä käyttäjänä voin kirjautua sivustolle.

`SELECT account.id FROM account WHERE account.username = ? AND account.password = ?;`
 
* Rekisteröityneenä käyttäjänä voin lisätä tuotteita sivustolle.

`INSERT INTO Product ('date_created', 'name', 'price', 'description', 'account_id', 'category_id') VALUES (CURRENT_TIMESTAMP, ?, ?, ?, ?);`

* Rekisteröityneenä käyttäjänä voin poistaa lisäämäni tuotteen sivustolta.
`DELETE FROM Order WHERE Order.product_id = ?;`
`DELETE FROM Product WHERE product.id = ?;`

* Rekisteröityneenä käyttäjänä voin muuttaa tuotteeni kuvausta.

`UPDATE Product SET Description = ? WHERE product.id = ?;`

* Rekisteröityneenä käyttäjänä voin nähdä lisäämäni tuotteet ja tilaukset.

`SELECT Order.id FROM Order JOIN product ON product.id = Order.product_id JOIN account ON account.id = product.account_id 
WHERE Order.account_id = ?;`

* Rekisteröityneenä käyttäjänä voin tilata tuotteen alustan kautta toiselta käyttäjältä.

`INSERT INTO Order (date_created, account_id, product_id) VALUES (CURRENT_TIMESTAMP, ?, ?);`
