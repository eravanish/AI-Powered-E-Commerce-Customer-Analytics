
--Top Selling Products--
SELECT product_name, SUM(revenue) AS total_sales
FROM ecommerce_sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;




--Top Cities by Sales--
SELECT city, SUM(revenue) AS city_sales
FROM ecommerce_sales
GROUP BY city
ORDER BY city_sales DESC;




--Profit by Category--
SELECT category, SUM(profit) AS total_profit
FROM ecommerce_sales
GROUP BY category
ORDER BY total_profit DESC;
