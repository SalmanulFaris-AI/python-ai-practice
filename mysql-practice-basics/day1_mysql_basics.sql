CREATE DATABASE school_db;
USE school_db;
CREATE TABLE students(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100),age INT);
INSERT INTO students(name,age)
VALUES('salman',22);
INSERT INTO students(name,age)
VALUES('Ali',21);
INSERT INTO students(name,age)
VALUES('Amina',23);
SELECT*FROM students;
DELETE FROM students
WHERE id=2;
UPDATE students
SET age=25
WHERE name='Ali';
UPDATE students
set id=2 
where name='Ali';
UPDATE students
SET id=3
WHERE name='Amina';
