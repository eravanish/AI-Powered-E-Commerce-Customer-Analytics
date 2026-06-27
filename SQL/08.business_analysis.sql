--Return Analysis--
SELECT category, COUNT(*) AS returned_orders
FROM ecommerce_sales
WHERE return_status = 'Returned'
GROUP BY category
ORDER BY returned_orders DESC;



--Most Used Payment Method--
SELECT payment_method, COUNT(*) AS total_orders
FROM ecommerce_sales
GROUP BY payment_method
ORDER BY total_orders DESC;



--Delivery Performance--
SELECT city, AVG(delivery_time) AS avg_delivery_days
FROM ecommerce_sales
GROUP BY city
ORDER BY avg_delivery_days DESC;