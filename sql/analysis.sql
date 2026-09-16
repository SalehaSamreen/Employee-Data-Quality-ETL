USE hr_analytics;


-- Overall HR summary
SELECT
    COUNT(*) AS total_employees,
    ROUND(AVG(Age), 2) AS average_age,
    ROUND(AVG(Salary_INR), 2) AS average_salary,
    ROUND(AVG(Years_at_Company), 2) AS average_years_at_company,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees;


-- Employee distribution and salary by department
SELECT
    Department,
    COUNT(*) AS employee_count,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Department
ORDER BY employee_count DESC;


-- Employee status overview
SELECT
    Employment_Status,
    COUNT(*) AS employee_count,
    ROUND(AVG(Salary_INR), 2) AS average_salary,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Employment_Status
ORDER BY employee_count DESC;


-- Performance rating overview
SELECT
    Performance_Rating,
    COUNT(*) AS employee_count,
    ROUND(AVG(Salary_INR), 2) AS average_salary,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Performance_Rating
ORDER BY employee_count DESC;


-- Employee status within each department
SELECT
    Department,
    Employment_Status,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department, Employment_Status
ORDER BY Department, employee_count DESC;


-- Salary and employee count by education
SELECT
    Education,
    COUNT(*) AS employee_count,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Education
ORDER BY average_salary DESC;


-- Leave patterns across departments
SELECT
    Department,
    COUNT(*) AS employee_count,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves,
    MAX(Leaves_Taken) AS highest_leaves
FROM employees
GROUP BY Department
ORDER BY average_leaves DESC;


-- Salary by years of experience in the company
SELECT
    Years_at_Company,
    COUNT(*) AS employee_count,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Years_at_Company
ORDER BY Years_at_Company;


-- Highest-paid employees
SELECT
    Employee_ID,
    Name,
    Department,
    Job_Title,
    Salary_INR,
    Years_at_Company
FROM employees
ORDER BY Salary_INR DESC
LIMIT 10;
