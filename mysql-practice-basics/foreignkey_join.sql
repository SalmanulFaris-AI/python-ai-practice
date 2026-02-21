-- Create Database
CREATE DATABASE shop_db;
USE shop_db;

-- Create Users Table (Parent Table)
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Create Orders Table (Child Table)
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert Users
INSERT INTO users (name) VALUES ('Salman');
INSERT INTO users (name) VALUES ('Arun');
INSERT INTO users (name) VALUES ('Amina');

-- Insert Orders
INSERT INTO orders (product_name, user_id) VALUES ('Laptop', 1);
INSERT INTO orders (product_name, user_id) VALUES ('Phone', 2);
INSERT INTO orders (product_name, user_id) VALUES ('Mouse', 1);

-- INNER JOIN
SELECT users.name, orders.product_name
FROM users
INNER JOIN orders
ON users.id = orders.user_id;

-- LEFT JOIN
SELECT users.name, orders.product_name
FROM users
LEFT JOIN orders
ON users.id = orders.user_id;
