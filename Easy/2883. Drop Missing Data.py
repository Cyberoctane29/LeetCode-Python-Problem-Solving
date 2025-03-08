# Problem 2883: Drop Missing Data
# Difficulty: Easy

# DataFrame `students`:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Problem Statement:
# Write a function to remove rows from the `students` DataFrame where the `name` column has missing values.

# Solution

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'], axis=0)

# Intuition:
# - I need to filter out rows where the `name` column contains missing values (NaN).
# - Only rows with valid names should be kept.

# Explanation:
# - `dropna(subset=['name'], axis=0)` removes rows where the `name` column has NaN values.
# - `axis=0` ensures that entire rows (not columns) are dropped.
# - The cleaned DataFrame is returned.
