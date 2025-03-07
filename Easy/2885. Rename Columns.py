# Problem 2885: Rename Columns
# Difficulty: Easy

# Problem Statement:
# Write a function to rename the columns in the `students` DataFrame as follows:
# - `id` → `student_id`
# - `first` → `first_name`
# - `last` → `last_name`
# - `age` → `age_in_years`

# Solution

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})

# Intuition:
# - I need to rename the columns to match the required format.
# - Using the `rename` function allows me to map old column names to new ones.

# Explanation:
# - The `rename` method is used with the `columns` parameter to change the column names.
# - Each column is assigned a new name based on the given mapping.
# - The updated DataFrame is returned with the modified column names.
