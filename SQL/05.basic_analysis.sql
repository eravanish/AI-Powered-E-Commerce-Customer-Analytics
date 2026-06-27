
--Total Revenue--
SELECT SUM(revenue) AS total_revenue
FROM ecommerce_sales;



--Total Profit--
SELECT SUM(profit) AS total_profit
FROM ecommerce_sales;



--Monthly Revenue Trend--
SELECT DATE_TRUNC('month',order_date) AS month, SUM(revenue) AS monthly_revenue
FROM ecommerce_sales
GROUP BY month
ORDER BY month;



