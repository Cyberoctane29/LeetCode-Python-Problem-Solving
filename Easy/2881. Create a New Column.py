# Problem 2881: Create a New Column
# Difficulty: Easy

# Problem Statement:
# Write a function to create a new column `bonus` in the DataFrame.
# The `bonus` column should contain values that are double the `salary` column.

# Solution

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

# Intuition:
# - I need to create a new column in the `employees` DataFrame.
# - The new column `bonus` should contain values that are twice the salary.

# Explanation:
# - `employees['bonus'] = employees['salary'] * 2` creates a new column `bonus`.
# - Each value in the `bonus` column is calculated as `salary * 2`.
# - The modified DataFrame is returned.
