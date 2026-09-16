import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Load cleaned data
df = pd.read_csv("data/cleaned/employee_data_cleaned.csv")

# Connect to MySQL
connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()

# Clear existing records before loading
cursor.execute("DELETE FROM employees")

# Insert cleaned data
insert_query = """
INSERT INTO employees (
    Employee_ID,
    Name,
    Age,
    Gender,
    City,
    Education,
    Department,
    Job_Title,
    Join_Date,
    Years_at_Company,
    Salary_INR,
    Performance_Rating,
    Leaves_Taken,
    Employment_Status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = [
    tuple(row)
    for row in df[
        [
            "Employee_ID",
            "Name",
            "Age",
            "Gender",
            "City",
            "Education",
            "Department",
            "Job_Title",
            "Join_Date",
            "Years_at_Company",
            "Salary_INR",
            "Performance_Rating",
            "Leaves_Taken",
            "Employment_Status"
        ]
    ].itertuples(index=False, name=None)
]

cursor.executemany(insert_query, data)

connection.commit()

print("Data loaded successfully.")
print("Rows loaded:", cursor.rowcount)

cursor.close()
connection.close()