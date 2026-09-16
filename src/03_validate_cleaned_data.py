import pandas as pd

# Load the cleaned HR dataset
df = pd.read_csv("data/cleaned/employee_data_cleaned.csv")

# Check dataset shape
print("Dataset shape:")
print(df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Check duplicate Employee IDs
print("\nDuplicate Employee IDs:")
print(df["Employee_ID"].duplicated().sum())

# Check performance ratings
print("\nPerformance ratings:")
print(df["Performance_Rating"].value_counts())

# Check salary values
print("\nSalary statistics:")
print(df["Salary_INR"].describe())

# Check Join_Date
df["Join_Date"] = pd.to_datetime(df["Join_Date"])

print("\nInvalid Join_Date values:")
print(df["Join_Date"].isna().sum())

print("\nValidation completed.")