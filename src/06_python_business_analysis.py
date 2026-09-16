import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Connect to MySQL
connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

print("Connected to MySQL.")

# Load employee data from MySQL
query = "SELECT * FROM employees"

df = pd.read_sql(query, connection)

print("\nEmployee data loaded.")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# Overall employee summary
print("\n--- Overall Summary ---")

print("Average age:", round(df["Age"].mean(), 2))
print("Average salary:", round(df["Salary_INR"].mean(), 2))
print("Average years at company:", round(df["Years_at_Company"].mean(), 2))
print("Average leaves:", round(df["Leaves_Taken"].mean(), 2))


# Department analysis
print("\n--- Department Analysis ---")

department_analysis = (
    df.groupby("Department")
    .agg(
        employee_count=("Employee_ID", "count"),
        average_salary=("Salary_INR", "mean")
    )
    .round(2)
    .sort_values("employee_count", ascending=False)
)

print(department_analysis)


# Employment status analysis
print("\n--- Employment Status Analysis ---")

status_analysis = (
    df.groupby("Employment_Status")
    .agg(
        employee_count=("Employee_ID", "count"),
        average_salary=("Salary_INR", "mean"),
        average_leaves=("Leaves_Taken", "mean")
    )
    .round(2)
    .sort_values("employee_count", ascending=False)
)

print(status_analysis)


# Performance analysis
print("\n--- Performance Analysis ---")

performance_analysis = (
    df.groupby("Performance_Rating")
    .agg(
        employee_count=("Employee_ID", "count"),
        average_salary=("Salary_INR", "mean"),
        average_leaves=("Leaves_Taken", "mean")
    )
    .round(2)
    .sort_values("employee_count", ascending=False)
)

print(performance_analysis)


# Highest-paid employees
print("\n--- Top 10 Highest-Paid Employees ---")

top_paid = (
    df[
        [
            "Employee_ID",
            "Name",
            "Department",
            "Job_Title",
            "Salary_INR",
            "Years_at_Company"
        ]
    ]
    .sort_values("Salary_INR", ascending=False)
    .head(10)
)

print(top_paid.to_string(index=False))


connection.close()

print("\nAnalysis completed.")
