"""Data-quality tests for the cleaned HR dataset. Run from repo root: pytest -v"""
from pathlib import Path
import pandas as pd
import pytest

CSV = Path(__file__).resolve().parents[1] / "data" / "cleaned" / "employee_data_cleaned.csv"
EXPECTED_COLUMNS = [
    "Employee_ID", "Name", "Age", "Gender", "City", "Education", "Department",
    "Job_Title", "Join_Date", "Years_at_Company", "Salary_INR",
    "Performance_Rating", "Leaves_Taken", "Employment_Status",
]
VALID_RATINGS = {"Excellent", "Good", "Average", "Poor", "Not Rated"}
VALID_STATUS = {"Active", "Terminated", "Resigned"}


@pytest.fixture(scope="module")
def df():
    return pd.read_csv(CSV)


def test_shape(df):
    assert df.shape == (1000, 14)


def test_expected_columns(df):
    assert list(df.columns) == EXPECTED_COLUMNS


def test_no_missing_values(df):
    assert df.isna().sum().sum() == 0


def test_no_duplicates(df):
    assert not df.duplicated().any()
    assert df["Employee_ID"].is_unique


def test_salary_positive_numeric(df):
    assert pd.api.types.is_numeric_dtype(df["Salary_INR"])
    assert (df["Salary_INR"] > 0).all()


def test_rating_categories(df):
    assert set(df["Performance_Rating"].unique()) <= VALID_RATINGS


def test_employment_status(df):
    assert set(df["Employment_Status"].unique()) <= VALID_STATUS


def test_join_date_valid_and_not_future(df):
    dates = pd.to_datetime(df["Join_Date"], errors="coerce")
    assert dates.notna().all()
    assert (dates <= pd.Timestamp.today()).all()


def test_no_stray_whitespace(df):
    for col in df.select_dtypes(include=["object", "string"]):
        assert (df[col] == df[col].str.strip()).all(), col
