--Customer Retention--
SELECT customer_id, COUNT(customer_id) AS total_orders
FROM ecommerce_sales
GROUP BY customer_id
HAVING COUNT(order_id)>1;