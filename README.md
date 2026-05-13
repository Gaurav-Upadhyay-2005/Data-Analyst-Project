# Data-Analyst-Project

# Sales Data Cleaning Project

## Project Overview

This project is a Data Cleaning and Data Preparation task created using Python, Pandas, and MySQL.

The project connects to a MySQL database, reads multiple tables, merges them into a single dataset, performs data cleaning operations, and exports the cleaned data into an Excel file.

---

## Objectives

* Read data from MySQL database
* Merge multiple tables
* Identify and handle data quality issues
* Prepare clean data for analysis
* Export cleaned dataset

---

## Technologies Used

* Python
* Pandas
* MySQL
* OpenPyXL

---

## Database Tables Used

1. Products
2. Customers
3. Sales

---

## Data Cleaning Steps Performed

### 1. Merging Tables

* Merged sales, products, and customers tables using common IDs.

### 2. Dataset Understanding

* Displayed first few rows
* Checked shape of dataset
* Checked missing values
* Checked data types
* Checked duplicate rows
* Checked invalid ages
* Checked date range

### 3. Data Cleaning

* Removed duplicate rows
* Removed negative age values
* Converted sale_date column into datetime format
* Created total_sale_amount column
* Extracted month from sale_date

### 4. Export

* Exported cleaned dataset into Excel format.

---

## Output File

```text
cleaned_sales_data.xlsx
```

---

## Project Structure

```text
jforce_DA_task/
│
├── main.py
├── cleaned_sales_data.xlsx
├── Professional Sales Dashboard.pbix
README.md
```

---

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install pandas mysql-connector-python openpyxl
```

### Step 2: Configure MySQL Database

Update the database credentials inside main.py:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="store"
)
```

### Step 3: Run the Project

```bash
python main.py
```

---

## Features

* SQL database connectivity
* Data merging using Pandas
* Data cleaning workflow
* Feature engineering
* Excel export support

---


## Author

Gaurav Upadhyay
