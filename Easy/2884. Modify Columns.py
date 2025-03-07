# Problem 2884: Modify Columns
# Difficulty: Easy

# Problem Statement:
# Write a function to modify the `salary` column in the `employees` DataFrame by multiplying each value by 2.

# Solution

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

# Intuition:
# - I need to update the `salary` column by doubling each value.
# - The modified DataFrame should be returned with the updated salaries.

# Explanation:
# - I directly modify the `salary` column using `employees['salary'] = employees['salary'] * 2`.
# - This updates each salary in the DataFrame.
# - The modified DataFrame is returned.
