--Repeat Customers--
SELECT customer_id, COUNT(order_id) AS total_orders
FROM ecommerce_sales
GROUP BY customer_id
HAVING COUNT(order_id) >1
ORDER BY total_orders DESC;




--Average Customer Rating--
SELECT category, AVG(customer_rating) AS avg_rating
FROM ecommerce_sales
GROUP BY category
ORDER BY avg_rating DESC;