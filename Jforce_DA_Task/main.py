import pandas as pd
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="store"
)

# Read tables
products = pd.read_sql("SELECT * FROM products", conn)
customers = pd.read_sql("SELECT * FROM customers", conn)
sales = pd.read_sql("SELECT * FROM sales", conn)

# Merge tables
df = sales.merge(products, on="product_id")
df = df.merge(customers, on="customer_id")

'''understanding about the dataset before cleaning'''

# display the first few rows of the merged DataFrame

print(df.head())

# checking how much columns and rows we have in the merged DataFrame

print(df.shape)

# checking for missing values in the merged DataFrame

print(df.isnull().sum())

# checking the data types of each column in the merged DataFrame

print(df.dtypes)

# checking for duplicate rows in the merged DataFrame

print(df.duplicated().sum())

# checking for negative ages in the merged DataFrame

print((df["age"] < 0).sum())

# Checking the range of sale dates in the merged DataFrame
print(df["sale_date"].min())
print(df["sale_date"].max())

''' Data Cleaning '''

# Remove duplicates
df = df.drop_duplicates()

# Remove negative ages
df = df[df["age"] > 0]

# Convert date
df["sale_date"] = pd.to_datetime(df["sale_date"])

# Create new column
df["total_sale_amount"] = df["quantity_sold"] * df["price"]

# Extract month
df["month"] = df["sale_date"].dt.month

# Save cleaned data
df.to_excel("cleaned_sales_data.xlsx", index=False)

print("Data Cleaned Successfully")