CREATE DATABASE store_db;
USE store_db;
CREATE TABLE customers(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100)NOT NULL,city VARCHAR(50));
CREATE TABLE orders(id INT PRIMARY KEY AUTO_INCREMENT,product_name VARCHAR(50)NOT NULL,price INT,
customer_id INT,
FOREIGN KEY (customer_id) REFERENCES customers(id));
-- customers
INSERT INTO customers(name,city)VALUES('salman','Delhi');
INSERT INTO customers(name,city)VALUES('Arun','Mumbai');
INSERT INTO customers(name,city)VALUES('Amina','Chennai');
-- orders
INSERT INTO orders(product_name,price,customer_id)VALUES('Laptop',60000,1);
INSERT INTO orders(product_name,price,customer_id)VALUES('Mouse',500,1);
INSERT INTO orders(product_name,price,customer_id)VALUES('Keyboard',1500,2);


SELECT customers.name,COUNT(orders.id)AS Total_number_of_orders
FROM customers
LEFT JOIN orders 
ON customer_id=customers.id
GROUP BY customers.name;
SELECT customers.name,SUM(orders.price)AS Total_amount
FROM customers
LEFT JOIN orders 
ON customers.id=orders.customer_id
GROUP BY customers.name;
