import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("data/hr_analytics.db")

# Check table names
tables = connection.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("Tables:")
print(tables)

# Check employee table columns
columns = connection.execute(
    "PRAGMA table_info(employees)"
).fetchall()

print("\nEmployees table columns:")

for column in columns:
    print(column)

# Check first 5 employees
employees = connection.execute(
    "SELECT * FROM employees LIMIT 5"
).fetchall()

print("\nFirst 5 employees:")

for employee in employees:
    print(employee)

# Close the database connection
connection.close()