# Problem 2880: Select Data
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
# Write a function to return the name and age of the student with student_id = 101.

# Solution

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

# Intuition:
# - I need to filter the DataFrame to find the student with `student_id = 101`.
# - Once filtered, I only need to select the `name` and `age` columns.

# Explanation:
# - `students[students['student_id'] == 101]` filters the rows where `student_id` is 101.
# - `[['name', 'age']]` ensures that only the required columns (`name` and `age`) are selected.
# - The function returns the result as a DataFrame.
