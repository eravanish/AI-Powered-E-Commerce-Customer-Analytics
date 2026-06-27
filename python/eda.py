
import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns

# Load dataset
df = pd.read_csv("../dataset/ecommerce_india_10000.csv")

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Show first 5 rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Statistical summary
print("\nSUMMARY STATISTICS")
print(df.describe())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Total revenue
total_revenue = df["revenue"].sum()
print("\nTOTAL REVENUE:", total_revenue)

# Top 10 products
top_products = df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(10)

print("\nTOP PRODUCTS")
print(top_products)

# Plot top products
plt.figure(figsize=(12,6))
top_products.plot(kind='bar')

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()




# ------------------------ Monthly Revenue Trend ----------------------------

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_sales = df.groupby(df["order_date"].dt.month)["revenue"].sum()

monthly_sales.plot(kind='line')

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()







# ------------------Category Sales Analysis-----------------------

category_sales = df.groupby("category")["revenue"].sum()

category_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Category Wise Sales")
plt.ylabel("")
plt.show()






# ------------------------City Wise Sales---------------------------

city_sales = df.groupby("city")["revenue"].sum().sort_values(ascending=False).head(10)

city_sales.plot(kind='bar')

plt.title("Top Cities by Revenue")

plt.show()