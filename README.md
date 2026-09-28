# Employee Data Quality & HR Analytics ETL Pipeline

A practical data analytics project that demonstrates an end-to-end workflow for cleaning employee data, validating data quality, loading the cleaned dataset into MySQL, and performing HR analytics using SQL and Python.

The project focuses on turning a raw employee dataset into a clean, validated, database-ready dataset and extracting descriptive business insights from it.

---

## 📌 Project Overview

This project simulates a small HR analytics workflow using a synthetic employee dataset containing **1,000 employee records and 14 attributes**.

The raw dataset contains missing values that need to be identified and handled before analysis.

The project follows a complete ETL and analytics workflow:

```text
Raw Employee CSV
       ↓
Data Inspection
       ↓
Data Cleaning
       ↓
Data Validation
       ↓
Load Cleaned Data into MySQL
       ↓
SQL Analysis
       ↓
Python / Pandas Analysis
       ↓
Business Insights
```

The main objective is not only to analyze employee data, but also to demonstrate how data can be prepared and moved through a simple analytics pipeline.

---

## 🎯 Objectives

The project was built to demonstrate the following practical data analyst skills:

* Inspecting raw datasets using Python and Pandas
* Identifying missing values and data quality issues
* Cleaning and transforming data
* Applying documented rules for missing-value handling
* Validating cleaned data
* Connecting Python to MySQL
* Loading cleaned data into a relational database
* Writing SQL queries for business analysis
* Performing analysis using Pandas
* Extracting descriptive HR insights
* Structuring a reproducible analytics project

---

## 📊 Dataset

The project uses a **synthetic HR employee dataset**.

### Dataset Size

* **Rows:** 1,000 employees
* **Columns:** 14

### Columns

| Column               | Description                          |
| -------------------- | ------------------------------------ |
| `Employee_ID`        | Unique employee identifier           |
| `Name`               | Employee name                        |
| `Age`                | Employee age                         |
| `Gender`             | Employee gender                      |
| `City`               | Employee city                        |
| `Education`          | Education level                      |
| `Department`         | Employee department                  |
| `Job_Title`          | Employee job title                   |
| `Join_Date`          | Date the employee joined the company |
| `Years_at_Company`   | Years spent at the company           |
| `Salary_INR`         | Employee salary in INR               |
| `Performance_Rating` | Performance rating                   |
| `Leaves_Taken`       | Number of leaves taken               |
| `Employment_Status`  | Current employment status            |

> **Note:** The dataset is synthetic. The findings in this project describe this dataset and should not be interpreted as real-world HR statistics.

---

# 🔍 Step 1 — Inspect the Raw Data

The first stage was to understand the raw dataset before making any changes.

The script:

```text
src/01_inspect_data.py
```

was used to inspect:

* Dataset shape
* Missing values
* Duplicate rows
* Duplicate employee IDs
* Numeric statistics
* Category values
* Date ranges
* Basic data validity

### Initial Dataset

```text
Rows: 1000
Columns: 14
```

### Missing Values Found

| Column               | Missing Values |
| -------------------- | -------------: |
| `Salary_INR`         |             32 |
| `Performance_Rating` |             19 |
| Other columns        |              0 |

Therefore, the raw dataset contained:

**51 missing values in total.**

There were also:

```text
Duplicate rows: 0
Duplicate Employee IDs: 0
```

The salary values ranged from approximately:

```text
₹28,900 → ₹1,60,400
```

The dataset did not contain invalid join dates or obvious invalid values in the inspected fields.

---

# 🧹 Step 2 — Clean the Data

The cleaning process was implemented in:

```text
src/02_clean_data.py
```

The cleaning stage performs the following operations.

### 1. Remove unnecessary whitespace

Whitespace was removed from relevant text columns such as:

* Employee ID
* Name
* Gender
* City
* Education
* Department
* Job Title
* Performance Rating
* Employment Status

### 2. Handle missing salary values

There were **32 missing salary values**.

The median salary of the dataset was:

```text
₹67,250
```

The missing salary values were replaced using this median.

### Why median?

Salary data can contain relatively high values that can pull the average upward. Median is therefore a reasonable documented choice for this synthetic dataset.

This is a project-level handling decision rather than a universal HR rule.

In a real organization, missing salary values should first be investigated to understand why the values are missing before choosing an imputation strategy.

### 3. Handle missing performance ratings

There were **19 missing performance ratings**.

Instead of assigning an artificial rating, the missing values were represented as:

```text
Not Rated
```

This preserves the fact that no performance rating was available.

### 4. Convert `Join_Date`

The `Join_Date` column was converted into a proper datetime format.

### 5. Save the cleaned dataset

The cleaned dataset was saved to:

```text
data/cleaned/employee_data_cleaned.csv
```

---

# ✅ Step 3 — Validate the Cleaned Data

The cleaned dataset was validated using:

```text
src/03_validate_cleaned_data.py
```

The validation checked:

* Dataset shape
* Missing values
* Duplicate rows
* Duplicate employee IDs
* Performance rating categories
* Salary statistics
* Join date validity

### Validation Results

```text
Dataset shape: (1000, 14)

Missing values:
All columns → 0

Duplicate rows:
0

Duplicate Employee IDs:
0

Invalid Join_Date values:
0
```

After cleaning:

```text
Missing values: 0
Duplicate rows: 0
Duplicate Employee IDs: 0
```

The cleaned dataset was therefore ready to be loaded into MySQL.

---

# 🗄️ Step 4 — Connect Python to MySQL

The project uses **MySQL** as the database layer.

The connection was tested using:

```text
src/04_test_mysql_connection.py
```

The connection uses environment variables stored in:

```text
.env
```

The `.env` file contains local database credentials and is intentionally excluded from GitHub.

Example structure:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=hr_analytics
```

> Never commit the actual `.env` file or database password to GitHub.

---

# 🏗️ Step 5 — Create the MySQL Database and Table

The database schema is defined in:

```text
sql/schema.sql
```

The project creates a database named:

```text
hr_analytics
```

and an `employees` table containing the 14 employee attributes.

The `Employee_ID` column is used as the primary key.

The database structure allows the cleaned CSV data to be stored in a relational database instead of being analyzed only from a local file.

---

# 📥 Step 6 — Load Cleaned Data into MySQL

The cleaned dataset is loaded into MySQL using:

```text
src/05_load_to_mysql.py
```

The script:

1. Reads the cleaned CSV using Pandas
2. Connects to MySQL
3. Selects the `hr_analytics` database
4. Clears existing records from the `employees` table
5. Inserts the cleaned records
6. Commits the transaction
7. Reports the number of rows loaded

### Load Result

```text
Rows loaded: 1000
```

The data was then verified directly in MySQL using queries such as:

```sql
USE hr_analytics;

SELECT COUNT(*) AS total_employees
FROM employees;
```

Result:

```text
1000
```

The employee records were also checked using:

```sql
SELECT *
FROM employees
LIMIT 5;
```

---

# 📈 Step 7 — SQL Analysis

SQL analysis is stored in:

```text
sql/analysis.sql
```

The analysis covers several HR-related questions.

### Analyses included

1. Overall HR summary
2. Employee distribution by department
3. Average salary by department
4. Employment status overview
5. Performance rating overview
6. Employment status within departments
7. Salary by education level
8. Leave patterns by department
9. Salary by years at the company
10. Highest-paid employees

---

# 🧮 Step 8 — Python / Pandas Business Analysis

After loading the data into MySQL, the employee data was also analyzed using:

```text
src/06_python_business_analysis.py
```

The script:

1. Connects to MySQL
2. Loads the employee table into a Pandas DataFrame
3. Calculates overall statistics
4. Groups employees by department
5. Analyzes employment status
6. Analyzes performance ratings
7. Identifies the highest-paid employees

This demonstrates how SQL and Python/Pandas can be used together in an analytics workflow.

---

# 📊 Key Findings

The following findings were obtained from the cleaned dataset.

## Overall Employee Summary

| Metric                   |     Result |
| ------------------------ | ---------: |
| Total employees          |      1,000 |
| Average age              |      38.54 |
| Average salary           | ₹71,892.50 |
| Average years at company |       4.90 |
| Average leaves taken     |      15.15 |

---

## Department Analysis

| Department       | Employees | Average Salary |
| ---------------- | --------: | -------------: |
| Operations       |       174 |     ₹63,111.78 |
| Finance          |       157 |     ₹80,607.64 |
| Customer Support |       146 |     ₹49,149.32 |
| Engineering      |       141 |   ₹1,07,484.04 |
| Sales            |       136 |     ₹71,267.28 |
| Marketing        |       132 |     ₹70,286.36 |
| HR               |       114 |     ₹61,003.95 |

In this synthetic dataset, Engineering has the highest average salary among the listed departments, while Customer Support has the lowest average salary.

These differences are descriptive only and do not establish why salary differences exist.

---

## Employment Status

| Employment Status | Employees | Average Salary | Average Leaves |
| ----------------- | --------: | -------------: | -------------: |
| Active            |       649 |     ₹71,593.45 |          14.94 |
| Terminated        |       184 |     ₹71,288.59 |          15.50 |
| Resigned          |       167 |     ₹73,720.06 |          15.60 |

---

## Performance Rating

| Performance Rating | Employees | Average Salary | Average Leaves |
| ------------------ | --------: | -------------: | -------------: |
| Excellent          |       257 |     ₹73,151.75 |          15.63 |
| Good               |       247 |     ₹72,992.31 |          15.01 |
| Average            |       242 |     ₹71,869.21 |          14.81 |
| Poor               |       235 |     ₹69,565.96 |          15.08 |
| Not Rated          |        19 |     ₹69,634.21 |          16.05 |

The `Not Rated` category represents the 19 performance ratings that were missing in the original dataset.

---

## Education Analysis

| Education  | Employees | Average Salary |
| ---------- | --------: | -------------: |
| PhD        |       258 |     ₹72,791.47 |
| Bachelor's |       234 |     ₹72,244.66 |
| Diploma    |       277 |     ₹71,385.02 |
| Master's   |       231 |     ₹71,140.26 |

---

## Leave Patterns

| Department       | Employees | Average Leaves | Maximum Leaves |
| ---------------- | --------: | -------------: | -------------: |
| Engineering      |       141 |          15.75 |             30 |
| Sales            |       136 |          15.54 |             30 |
| Finance          |       157 |          15.43 |             30 |
| Marketing        |       132 |          15.28 |             30 |
| HR               |       114 |          15.07 |             30 |
| Customer Support |       146 |          14.86 |             30 |
| Operations       |       174 |          14.32 |             30 |

---

## Salary by Years at Company

| Years | Employees | Average Salary |
| ----: | --------: | -------------: |
|     1 |       116 |     ₹66,825.43 |
|     2 |       124 |     ₹67,561.29 |
|     3 |       111 |     ₹72,597.30 |
|     4 |       111 |     ₹73,075.23 |
|     5 |       115 |     ₹71,907.83 |
|     6 |       101 |     ₹74,057.92 |
|     7 |        97 |     ₹71,114.95 |
|     8 |       128 |     ₹77,867.58 |
|     9 |        96 |     ₹72,242.19 |
|    10 |         1 |     ₹43,800.00 |

The 10-year category contains only **one employee**, so it should not be interpreted as a meaningful salary trend.

---

# 🔎 Data Quality Summary

The main data-quality issue in the raw dataset was missing information.

```text
Raw records                  1,000
Raw columns                     14

Missing salaries                32
Missing performance ratings     19
Total missing values            51

Duplicate rows                   0
Duplicate Employee IDs           0

Cleaned records               1,000
Missing values after cleaning     0
```

### Missing-value handling

```text
Salary_INR
32 missing values
        ↓
Dataset median
₹67,250
        ↓
Missing salaries replaced
```

```text
Performance_Rating
19 missing values
        ↓
"Not Rated"
        ↓
Missing ratings represented explicitly
```

---

# 🔄 Complete ETL Workflow

The complete workflow of this project can be summarized as:

```text
                RAW DATA
                   │
                   ▼
        employee_data.csv
                   │
                   ▼
        ┌──────────────────┐
        │  Data Inspection  │
        │  Pandas / Python  │
        └──────────────────┘
                   │
                   │
          Identify issues
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 32 Missing Salary      19 Missing Rating
        │                     │
        ▼                     ▼
 Median Imputation       "Not Rated"
        │                     │
        └──────────┬──────────┘
                   ▼
        ┌──────────────────┐
        │   Data Cleaning   │
        └──────────────────┘
                   │
                   ▼
      employee_data_cleaned.csv
                   │
                   ▼
        ┌──────────────────┐
        │ Data Validation   │
        └──────────────────┘
                   │
          0 missing values
          0 duplicate IDs
          0 duplicate rows
                   │
                   ▼
        ┌──────────────────┐
        │      MySQL       │
        │   hr_analytics   │
        └──────────────────┘
                   │
                   ▼
             employees
                   │
          ┌────────┴────────┐
          ▼                 ▼
    SQL Analysis       Python/Pandas
          │                 │
          └────────┬────────┘
                   ▼
          Business Insights
```

---

# 📁 Project Structure

```text
Employee-Data-Quality-ETL/
│
├── data/
│   ├── raw/
│   │   └── employee_data.csv
│   │
│   └── cleaned/
│       └── employee_data_cleaned.csv
│
├── sql/
│   ├── schema.sql
│   └── analysis.sql
│
├── src/
│   ├── 01_inspect_data.py
│   ├── 02_clean_data.py
│   ├── 03_validate_cleaned_data.py
│   ├── 04_test_mysql_connection.py
│   ├── 05_load_to_mysql.py
│   └── 06_python_business_analysis.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

### Programming & Analysis

* Python
* Pandas

### Database

* MySQL

### SQL

* MySQL SQL
* Aggregations
* `GROUP BY`
* `ORDER BY`
* `COUNT`
* `AVG`
* `MAX`
* Filtering and sorting

### Python Libraries

* Pandas
* MySQL Connector
* python-dotenv

### Tools

* MySQL Workbench
* VS Code
* Git
* GitHub

---

# ▶️ How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/SalehaSamreen/Ecommerce-Analytics.git
```

Replace the repository URL with this project's GitHub repository URL after it is created/pushed.

Then move into the project folder:

```bash
cd Employee-Data-Quality-ETL
```

---

## 2. Create a Python virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure MySQL credentials

Create a local `.env` file containing:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=hr_analytics
```

Do not upload the `.env` file to GitHub.

---

## 5. Inspect the raw data

Run:

```bash
python src/01_inspect_data.py
```

This examines the raw employee dataset and identifies data-quality issues.

---

## 6. Clean the data

Run:

```bash
python src/02_clean_data.py
```

This creates:

```text
data/cleaned/employee_data_cleaned.csv
```

---

## 7. Validate the cleaned data

Run:

```bash
python src/03_validate_cleaned_data.py
```

The validation should show:

```text
Missing values → 0
Duplicate rows → 0
Duplicate Employee IDs → 0
Invalid Join_Date values → 0
```

---

## 8. Test MySQL connection

Make sure MySQL Server is running and run:

```bash
python src/04_test_mysql_connection.py
```

Expected result:

```text
MySQL connection successful.
```

---

## 9. Create the database and table

Run the SQL statements from:

```text
sql/schema.sql
```

This creates:

```text
hr_analytics
    └── employees
```

---

## 10. Load the cleaned data into MySQL

Run:

```bash
python src/05_load_to_mysql.py
```

Expected result:

```text
Data loaded successfully.
Rows loaded: 1000
```

---

## 11. Run SQL analysis

Open:

```text
sql/analysis.sql
```

Select the required queries in MySQL Workbench and execute them.

The queries provide analysis of:

* Employee distribution
* Departments
* Salaries
* Employment status
* Performance
* Education
* Leave patterns
* Years at company
* Highest-paid employees

---

## 12. Run Python business analysis

Run:

```bash
python src/06_python_business_analysis.py
```

This retrieves employee data from MySQL and performs additional analysis using Pandas.

---

# 🔐 Security

Database credentials are stored locally in:

```text
.env
```

The `.env` file should not be committed to GitHub.

The project should use `.gitignore` to prevent accidental credential exposure.

No database password is included in this repository.

---

# ⚠️ Limitations

This project uses a **synthetic HR dataset**, so the results should not be treated as actual organizational HR findings.

The project demonstrates the technical workflow of:

```text
Data → Cleaning → Validation → Database → Analysis
```

rather than attempting to model a real company's workforce.

The median salary imputation used in this project is a documented handling decision for this dataset. In a real HR environment, missing salary data would require investigation into the source and reason for the missing values before selecting an appropriate treatment.

Similarly, `Not Rated` indicates that a performance rating was unavailable; it does not represent an actual performance assessment.

---

# 💡 What This Project Demonstrates

This project demonstrates an end-to-end beginner-to-intermediate data analytics workflow:

```text
Python / Pandas
       ↓
Data Quality
       ↓
ETL
       ↓
MySQL
       ↓
SQL
       ↓
Python Analysis
       ↓
Business Insights
```

Rather than analyzing a CSV in isolation, the project demonstrates how cleaned data can move from a raw source into a database and then be used for analytical queries.

---

# 📌 Project Outcome

Starting with a raw dataset of **1,000 employee records**, the project:

* Identified **51 missing values**
* Handled **32 missing salary values** using the dataset median of **₹67,250**
* Represented **19 missing performance ratings** as `Not Rated`
* Validated the cleaned dataset
* Confirmed **0 duplicate employee IDs**
* Confirmed **0 duplicate rows**
* Loaded all **1,000 cleaned records into MySQL**
* Created multiple SQL analyses
* Performed additional analysis using Python and Pandas
* Extracted descriptive HR insights from the cleaned data

The final result is a reproducible HR analytics ETL pipeline that connects **data cleaning, database management, SQL analysis, and Python-based analytics** in one project.
