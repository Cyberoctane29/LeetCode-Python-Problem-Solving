# Problem 2879: Display the First Three Rows
# Difficulty: Easy

# DataFrame `employees`:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+

# Problem Statement:
# Write a function to return the first three rows of the given DataFrame `employees`.

# Solution

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[:3]

# Intuition:
# - I need to retrieve the first three rows from the given DataFrame.
# - The `.iloc[]` function allows me to select rows based on their index positions.
# - Using `.iloc[:3]` extracts the first three rows.

# Explanation:
# - `.iloc[:3]` selects the first three rows by slicing from index `0` to `2` (Python indexing is zero-based).
# - This method ensures that exactly the first three rows are returned.
# - The function returns the result as a DataFrame, preserving the original structure.
