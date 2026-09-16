-- 1. Which departments have the highest employee count?
SELECT
    Department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Department
ORDER BY employee_count DESC;


-- 2. Which departments have the highest average salary?
SELECT
    Department,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Department
ORDER BY average_salary DESC;


-- 3. Which departments have the most employees who left?
SELECT
    Department,
    COUNT(*) AS employees_left
FROM employees
WHERE Employment_Status IN ('Resigned', 'Terminated')
GROUP BY Department
ORDER BY employees_left DESC;


-- 4. Which performance rating has the highest average salary?
SELECT
    Performance_Rating,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Performance_Rating
ORDER BY average_salary DESC;


-- 5. What is the average number of leaves taken by employment status?
SELECT
    Employment_Status,
    ROUND(AVG(Leaves_Taken), 2) AS average_leaves
FROM employees
GROUP BY Employment_Status
ORDER BY average_leaves DESC;


-- 6. What is the average salary for each tenure level?
SELECT
    Years_at_Company,
    COUNT(*) AS employee_count,
    ROUND(AVG(Salary_INR), 2) AS average_salary
FROM employees
GROUP BY Years_at_Company
ORDER BY Years_at_Company;