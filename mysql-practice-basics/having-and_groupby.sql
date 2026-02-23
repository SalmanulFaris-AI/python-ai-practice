SELECT customers.name,COUNT(orders.id)AS Total_orders,SUM(orders.price)AS Total_amount
FROM customers JOIN orders ON customers.id=customer_id 
GROUP BY customers.name
HAVING COUNT(orders.id) >=2 AND SUM(orders.price) >10000
ORDER BY total_amount DESC;
