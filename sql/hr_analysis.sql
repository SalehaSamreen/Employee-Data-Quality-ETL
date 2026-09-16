-- Total employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Active employees
SELECT COUNT(*) AS active_employees
FROM employees
WHERE Employment_Status = 'Active';

-- Resigned employees
SELECT COUNT(*) AS resigned_employees
FROM employees
WHERE Employment_Status = 'Resigned';

-- Terminated employees
SELECT COUNT(*) AS terminated_employees
FROM employees
WHERE Employment_Status = 'Terminated';

-- Average salary
SELECT ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees;

-- Average age
SELECT ROUND(AVG(Age), 2) AS average_age
FROM employees;

-- Employee count by department
SELECT
    Department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department
ORDER BY employee_count DESC;


-- Average salary by department
SELECT
    Department,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Department
ORDER BY average_salary DESC;


-- Employment status by department
SELECT
    Department,
    Employment_Status,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department, Employment_Status
ORDER BY Department, employee_count DESC;

-- Employee count by performance rating
SELECT
    Performance_Rating,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Performance_Rating
ORDER BY employee_count DESC;


-- Average salary by performance rating
SELECT
    Performance_Rating,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Performance_Rating
ORDER BY average_salary DESC;


-- Performance rating by department
SELECT
    Department,
    Performance_Rating,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department, Performance_Rating
ORDER BY Department, employee_count DESC;

-- Average salary by employment status
SELECT
    Employment_Status,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Employment_Status
ORDER BY average_salary DESC;


-- Average salary by years at company
SELECT
    Years_at_Company,
    ROUND(AVG(Salary_INR), 2) AS average_salary,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Years_at_Company
ORDER BY Years_at_Company;


-- Average leaves by employment status
SELECT
    Employment_Status,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Employment_Status
ORDER BY average_leaves DESC;


-- Average leaves by performance rating
SELECT
    Performance_Rating,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Performance_Rating
ORDER BY average_leaves DESC;