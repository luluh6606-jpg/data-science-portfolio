import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
data = pd.read_csv("sales_data.csv")

#Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Display basic information
print("\nDataset Information")
print(data.info())

# Check for missing values
print("\nMissing Values.")
print(data.isnull().sum())

# Calculate total sales
data['Total_Sales'] = data['Quantity'] * data['Unit_Price']
print("\nSales summary")
print("Total Revenue:", data['Total_Sales'].sum())
print("Average Sale:", data['Total_Sales'].mean())
print("Maximum Sale:", data['Total_Sales'].max())

# Sales by Product
product_sales = data.groupby('Product')["Total_Sales"].sum().sort_values(ascending=False)

print("\nSales by Product")
print(product_sales)

# Sales by Region
region_sales = data.groupby('Region')["Total_Sales"].sum().sort_values(ascending=False)

print("\nSales by Region")
print(region_sales)

# Visualize sales by region
plt.figure(figsize=(10, 4))
region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Visualize sales by product
plt.figure(figsize=(10, 4))
product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Sales trend over time
daily_sales = data.groupby('Date')["Total_Sales"].sum()

print("\nDaily Sales Trend over Time")
print(daily_sales)

# Visualize Sales trend over time
plt.figure(figsize=(10,5))
daily_sales.plot(kind="line")

plt.title("Daily Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

data["Total_Sales"]=data["Quantity"]*data["Unit_Price"]

category_sales = data.groupby('Category')["Total_Sales"].sum().sort_values(ascending=False)

print("\nSales by Category")
print(category_sales)

# Visualize sales by category
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Key insights
best_product=product_sales.idxmax()
best_region=region_sales.idxmax()

print("\nKey Insights:")
print("Best-selling product:", best_product)
print("Highest-revenue region:", best_region)
print("Total revenue:",data["Total_Sales"].sum())
