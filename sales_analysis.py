import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_dataset.csv")

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

region_profit.plot(kind='bar')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()
