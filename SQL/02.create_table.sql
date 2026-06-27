
CREATE TABLE ecommerce_sales (
order_id VARCHAR(50),
customer_id VARCHAR(50),
order_date DATE,
category VARCHAR(100),
product_name VARCHAR(200),
city VARCHAR(100),
payment_method VARCHAR(50),
quantity INT,
revenue NUMERIC,
discount NUMERIC,
profit NUMERIC,
delivery_time INT,
customer_rating NUMERIC,
return_status VARCHAR(20)
);
