CREATE DATABASE office_db;
USE office_db;
CREATE TABLE users(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100)NOT NULL,email VARCHAR(100) UNIQUE,
age INT CHECK(age>=18),country VARCHAR(50)DEFAULT 'india');
SELECT*FROM users;
INSERT INTO users(name,email,age,country)
VALUES('salman','sammufari123@gmail.com',19,'brazil');
INSERT INTO users(name,email,age,country)
VALUES('arun','sammufari123@gmail.com',19,'brazil');
INSERT INTO users(name,email,age,country)
VALUES('arun','arun123@gmail.com',17,'brazil');
INSERT INTO users(name,email,age)
VALUES('arun','arun123@gmail.com',19);
