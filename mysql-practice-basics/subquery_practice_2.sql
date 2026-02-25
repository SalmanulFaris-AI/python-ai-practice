-- SHOW CUSTOMERS WHOSE TOTAL SPENDING IS GREATER THAN  AVERAGE ORDER PRICE

SELECT name,SUM(price)AS total_spending FROM customers JOIN orders ON customers.id=orders.customer_id
GROUP BY name
HAVING SUM(price) >(SELECT AVG(price) FROM orders);
