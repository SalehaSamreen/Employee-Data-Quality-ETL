import pandas as pd

# Load the raw HR dataset
df = pd.read_csv("data/raw/employee_data.csv")

# Display the first 5 rows
print(df.head())

# Display number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display data types
print("\nData types:")
print(df.dtypes)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate Employee IDs
print("\nDuplicate Employee IDs:")
print(df["Employee_ID"].duplicated().sum())

# Check completely duplicated rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Check numeric column statistics
print("\nNumeric statistics:")
print(df.describe())

# Check unique values in categorical columns
categorical_columns = [
    "Gender",
    "Education",
    "Department",
    "Performance_Rating",
    "Employment_Status"
]

print("\nUnique categorical values:")

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].unique())

# Inspect Join_Date values
print("\nJoin_Date sample:")
print(df["Join_Date"].head(10))

# Check Join_Date range
print("\nJoin_Date range:")
print("Earliest:", df["Join_Date"].min())
print("Latest:", df["Join_Date"].max())

# Check for potentially invalid numeric values
print("\nInvalid numeric values:")

print("Age <= 0:", (df["Age"] <= 0).sum())
print("Years_at_Company < 0:", (df["Years_at_Company"] < 0).sum())
print("Salary_INR <= 0:", (df["Salary_INR"] <= 0).sum())
print("Leaves_Taken < 0:", (df["Leaves_Taken"] < 0).sum())

# Check for whitespace in text columns
text_columns = [
    "Gender",
    "Education",
    "Department",
    "Job_Title",
    "Performance_Rating",
    "Employment_Status"
]

print("\nText formatting check:")

for column in text_columns:
    print(f"\n{column}:")
    print(
        "Leading/trailing spaces:",
        df[column].astype(str).str.strip().ne(df[column].astype(str)).sum()
    )

# Check for invalid categorical values
expected_values = {
    "Gender": ["Male", "Female"],
    "Education": ["Bachelor's", "Master's", "PhD", "Diploma"],
    "Department": [
        "Marketing",
        "Operations",
        "HR",
        "Sales",
        "Customer Support",
        "Engineering",
        "Finance"
    ],
    "Performance_Rating": [
        "Excellent",
        "Good",
        "Average",
        "Poor"
    ],
    "Employment_Status": [
        "Active",
        "Resigned",
        "Terminated"
    ]
}

print("\nInvalid categorical values:")

for column, allowed_values in expected_values.items():
    invalid_values = df.loc[
        ~df[column].isin(allowed_values) & df[column].notna(),
        column
    ]

    print(f"{column}:", len(invalid_values))

# Check for blank Employee_ID and Name values
print("\nBlank Employee_ID values:")
print((df["Employee_ID"].astype(str).str.strip() == "").sum())

print("\nBlank Name values:")
print((df["Name"].astype(str).str.strip() == "").sum())

# Check for invalid Join_Date values
parsed_dates = pd.to_datetime(df["Join_Date"], errors="coerce")

print("\nInvalid Join_Date values:")
print(parsed_dates.isna().sum())

# Check for future Join_Date values
today = pd.Timestamp.today()

print("\nFuture Join_Date values:")
print((parsed_dates > today).sum())

# Check Employee_ID format
valid_employee_ids = df["Employee_ID"].astype(str).str.match(r"^EMP\d{4}$")

print("\nInvalid Employee_ID format:")
print((~valid_employee_ids).sum())

# Check reasonable age range
print("\nAge outside 18-65:")
print((~df["Age"].between(18, 65)).sum())

# Check leave range
print("\nLeaves_Taken outside 0-30:")
print((~df["Leaves_Taken"].between(0, 30)).sum())

# Check salary range
print("\nSalary outside 20,000-500,000:")
print(
    (
        (df["Salary_INR"] < 20000)
        | (df["Salary_INR"] > 500000)
    ).sum()
)