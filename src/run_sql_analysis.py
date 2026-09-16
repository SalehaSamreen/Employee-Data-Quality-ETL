import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("data/hr_analytics.db")

# Total employees
query = """
SELECT COUNT(*) AS total_employees
FROM employees
"""

result = connection.execute(query).fetchone()

print("Total employees:", result[0])

# Active employees
query = """
SELECT COUNT(*) AS active_employees
FROM employees
WHERE Employment_Status = 'Active'
"""

result = connection.execute(query).fetchone()

print("Active employees:", result[0])

# Resigned employees
query = """
SELECT COUNT(*) AS resigned_employees
FROM employees
WHERE Employment_Status = 'Resigned'
"""

result = connection.execute(query).fetchone()

print("Resigned employees:", result[0])

# Terminated employees
query = """
SELECT COUNT(*) AS terminated_employees
FROM employees
WHERE Employment_Status = 'Terminated'
"""

result = connection.execute(query).fetchone()

print("Terminated employees:", result[0])

# Average salary
query = """
SELECT ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
"""

result = connection.execute(query).fetchone()

print("Average salary:", result[0])

# Average age
query = """
SELECT ROUND(AVG(Age), 2) AS average_age
FROM employees
"""

result = connection.execute(query).fetchone()

print("Average age:", result[0])

# Employee count by department
query = """
SELECT
    Department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department
ORDER BY employee_count DESC
"""

results = connection.execute(query).fetchall()

print("\nEmployee count by department:")

for row in results:
    print(row)


# Average salary by department
query = """
SELECT
    Department,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Department
ORDER BY average_salary DESC
"""

results = connection.execute(query).fetchall()

print("\nAverage salary by department:")

for row in results:
    print(row)


# Employment status by department
query = """
SELECT
    Department,
    Employment_Status,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department, Employment_Status
ORDER BY Department, employee_count DESC
"""

results = connection.execute(query).fetchall()

print("\nEmployment status by department:")

for row in results:
    print(row)

# Employee count by performance rating
query = """
SELECT
    Performance_Rating,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Performance_Rating
ORDER BY employee_count DESC
"""

results = connection.execute(query).fetchall()

print("\nEmployee count by performance rating:")

for row in results:
    print(row)


# Average salary by performance rating
query = """
SELECT
    Performance_Rating,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Performance_Rating
ORDER BY average_salary DESC
"""

results = connection.execute(query).fetchall()

print("\nAverage salary by performance rating:")

for row in results:
    print(row)


# Performance rating by department
query = """
SELECT
    Department,
    Performance_Rating,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department, Performance_Rating
ORDER BY Department, employee_count DESC
"""

results = connection.execute(query).fetchall()

print("\nPerformance rating by department:")

for row in results:
    print(row)

# Average salary by employment status
query = """
SELECT
    Employment_Status,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Employment_Status
ORDER BY average_salary DESC
"""

results = connection.execute(query).fetchall()

print("\nAverage salary by employment status:")

for row in results:
    print(row)


# Average salary by years at company
query = """
SELECT
    Years_at_Company,
    ROUND(AVG(Salary_INR), 2) AS average_salary,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Years_at_Company
ORDER BY Years_at_Company
"""

results = connection.execute(query).fetchall()

print("\nAverage salary by years at company:")

for row in results:
    print(row)


# Average leaves by employment status
query = """
SELECT
    Employment_Status,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Employment_Status
ORDER BY average_leaves DESC
"""

results = connection.execute(query).fetchall()

print("\nAverage leaves by employment status:")

for row in results:
    print(row)


# Average leaves by performance rating
query = """
SELECT
    Performance_Rating,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Performance_Rating
ORDER BY average_leaves DESC
"""

results = connection.execute(query).fetchall()

print("\nAverage leaves by performance rating:")

for row in results:
    print(row)

# Close the database connection
connection.close()