# (1) Customer Segmentation {RFM- 
#                    Recency(Last Purchase), Frequency(No of Orders), Monetary(Total Spending) Analysis}

import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/ecommerce_india_10000.csv")

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Create RFM table
rfm = df.groupby("customer_id").agg({
    "order_date": lambda x: (df["order_date"].max() - x.max()).days,
    "order_id": "count",
    "revenue": "sum"
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

# Show output
print(rfm.head())





# (2) Correlation Analysis :-
#                        Find relationship between: discount, revenue, profit, rating

import seaborn as sns
import matplotlib.pyplot as plt

correlation = df[["revenue", "profit", "discount", "customer_rating"]].corr()
print(correlation)

plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True)
plt.title("Correlation Matrix")
plt.show()





# (3) Monthly Sales Forecasting :-

from sklearn.linear_model import LinearRegression
import numpy as np

# Convert column names to lowercase
df.columns = df.columns.str.lower()

monthly_sales = df.groupby("order_date")["revenue"].sum().reset_index()
monthly_sales["day_number"] = np.arange(len(monthly_sales))

X = monthly_sales[["day_number"]]
y = monthly_sales["revenue"]

model = LinearRegression()
model.fit(X, y)

future_days = np.array([[len(monthly_sales) + 30]])
prediction = model.predict(future_days)

print("Predicted Future Revenue:", prediction[0])





# (4) Top Customers Analysis :-

# Convert column names to lowercase
df.columns = df.columns.str.lower()

top_customers = df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False).head(10)
print(top_customers)




# (5) Predicted Future Revenue :-

from sklearn.linear_model import LinearRegression
import numpy as np

daily_sales = df.groupby("order_date")["revenue"].sum().reset_index()

daily_sales["day_number"] = np.arange(len(daily_sales))

X = daily_sales[["day_number"]]
y = daily_sales["revenue"]

model = LinearRegression()
model.fit(X, y)

future_day = np.array([[len(daily_sales) + 30]])

prediction = model.predict(future_day)

print("Predicted Future Revenue:", prediction[0])





# -------------Revenue Trend :----------------

monthly_sales.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.show()
