CREATE DATABASE IF NOT EXISTS hr_analytics;

USE hr_analytics;

CREATE TABLE IF NOT EXISTS employees (
    Employee_ID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Education VARCHAR(50) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Job_Title VARCHAR(100) NOT NULL,
    Join_Date DATE NOT NULL,
    Years_at_Company INT NOT NULL,
    Salary_INR DECIMAL(10,2) NOT NULL,
    Performance_Rating VARCHAR(20) NOT NULL,
    Leaves_Taken INT NOT NULL,
    Employment_Status VARCHAR(20) NOT NULL
);