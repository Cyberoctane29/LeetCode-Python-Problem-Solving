# Problem 2886: Change Data Type
# Difficulty: Easy

# DataFrame `students`:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# | grade       | float  |
# +-------------+--------+

# Problem Statement:
# Write a function to convert the `grade` column from float to integer in the `students` DataFrame.

# Solution

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

# Intuition:
# - The `grade` column is stored as floats, but it should be in integer format.
# - I need to convert it using the `astype(int)` function.

# Explanation:
# - The `astype(int)` method changes the `grade` column's data type from float to integer.
# - The modified DataFrame is then returned with the corrected data type.
