# Problem 627: Swap Salary
# Difficulty: Easy

# Table: Salary
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# | sex         | ENUM     |
# | salary      | int      |
# +-------------+----------+
# id is the primary key for this table.
# The sex column holds values 'm' or 'f' for male and female employees respectively.

# Problem Statement:
# Write a solution to swap all 'f' and 'm' values in the sex column (change 'f' to 'm' and 'm' to 'f')
# without using any intermediate tables or select statements — performing an in-place update.

# Solution

import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    # I handle the case where the input DataFrame might be empty
    if salary.empty:
        return salary
    # I use the replace() function with inplace=True to swap 'f' with 'm' and 'm' with 'f' directly in the DataFrame
    salary['sex'].replace({'f': 'm', 'm': 'f'}, inplace=True)
    # I return the updated DataFrame
    return salary

# Intuition for Solution:
# - I need to swap 'm' with 'f' and 'f' with 'm' in the sex column.
# - I use the Pandas replace() method to directly swap these values.
# - I apply this update in-place to avoid creating temporary tables or additional DataFrames.

# Explanation for Solution:
# - I first check if the DataFrame is empty to avoid unnecessary operations.
# - I apply the replace() method with a mapping dictionary to swap 'f' with 'm' and vice versa.
# - I use inplace=True to modify the original DataFrame.
# - I return the updated DataFrame with swapped values.