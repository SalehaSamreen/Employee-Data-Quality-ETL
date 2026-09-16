import pandas as pd
import sqlite3

# Load the cleaned HR dataset
df = pd.read_csv("data/cleaned/employee_data_cleaned.csv")

# Connect to SQLite database
connection = sqlite3.connect("data/hr_analytics.db")

# Load the data into a database table
df.to_sql("employees", connection, if_exists="replace", index=False)

# Check number of records in the table
result = pd.read_sql("SELECT COUNT(*) AS total_employees FROM employees", connection)

print("Data loaded into SQLite successfully.")
print("\nEmployee count:")
print(result)

# Close the database connection
connection.close()