# Problem 1527: Patients With a Condition
# Difficulty: Easy

# Table: Patients
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | patient_id   | int     |
# | patient_name | varchar |
# | conditions   | varchar |
# +--------------+---------+
# patient_id is the primary key (column with unique values) for this table.
# 'conditions' contains 0 or more codes separated by spaces.

# Problem Statement:
# - Find patients who have Type I Diabetes.
# - Type I Diabetes always starts with the prefix "DIAB1".
# - Return the `patient_id`, `patient_name`, and `conditions`.

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.loc[
        patients['conditions'].str.contains(r"(^|\s)DIAB1", regex=True), 
        ['patient_id', 'patient_name', 'conditions']
    ]

# Intuition:
# - The `conditions` column contains multiple condition codes separated by spaces.
# - We need to find patients whose `conditions` contain "DIAB1" as a standalone condition or as the first condition.
# - The condition "DIAB1" should be either at the beginning of the string or preceded by a space.

# Explanation:
# - `str.contains(r"(^|\s)DIAB1", regex=True)`:
#   - `^|\s`: Ensures "DIAB1" appears either at the start (`^`) or after a space (`\s`).
#   - `DIAB1`: Matches the required condition prefix.
#   - Using `regex=True` ensures a proper match instead of a simple substring search.
# - The function filters the DataFrame and returns only the required columns: `patient_id`, `patient_name`, and `conditions`.
