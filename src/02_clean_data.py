import pandas as pd

# Load the raw HR dataset
df = pd.read_csv("data/raw/employee_data.csv")

# Remove extra spaces from text columns
text_columns = [
    "Employee_ID",
    "Name",
    "Gender",
    "City",
    "Education",
    "Department",
    "Job_Title",
    "Performance_Rating",
    "Employment_Status"
]

for column in text_columns:
    df[column] = df[column].str.strip()

# Fill missing salary values with the median salary
salary_median = df["Salary_INR"].median()
df["Salary_INR"] = df["Salary_INR"].fillna(salary_median)

# Fill missing performance ratings
df["Performance_Rating"] = df["Performance_Rating"].fillna("Not Rated")

# Convert Join_Date to date format
df["Join_Date"] = pd.to_datetime(df["Join_Date"])

# Create the cleaned data folder
import os
os.makedirs("data/cleaned", exist_ok=True)

# Save the cleaned dataset
df.to_csv("data/cleaned/employee_data_cleaned.csv", index=False)

print("Cleaning completed.")
print("Rows:", len(df))
print("Missing salary values:", df["Salary_INR"].isnull().sum())
print("Missing performance ratings:", df["Performance_Rating"].isnull().sum())
print("Cleaned file saved to data/cleaned/employee_data_cleaned.csv")