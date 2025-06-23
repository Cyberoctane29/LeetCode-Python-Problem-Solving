# Problem 177: Nth Highest Salary
# Difficulty: Medium

# Table: Employee
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.

# Problem Statement:
# Write a function to find the nth highest distinct salary from the Employee table.
# If there are less than n distinct salaries, return null (None in Pandas).

# Solution

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # I first check if the given N is less than 1; if so, I immediately return None
    if N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # I extract the unique salary values and sort them in descending order
    result_series = pd.Series(employee['salary'].unique()).sort_values(ascending=False)
    
    # I check if the number of unique salaries is at least N
    if len(result_series) >= N:
        # If so, I pick the nth highest salary (zero-based index N-1)
        nth_highest = result_series.iloc[N-1]
    else:
        # Otherwise, I set the result to None
        nth_highest = None
    
    # I return the result as a DataFrame with the required column name format
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})

# Intuition:
# I need to find the Nth largest unique salary from the Employee table.
# To do this, I first extract the unique salaries, then sort them in descending order.
# If at least N unique salaries exist, I select the Nth one; otherwise, I return None.

# Explanation:
# I use unique() to get distinct salaries from the salary column.
# I convert these into a Pandas Series and sort it in descending order.
# I check the length of this Series:
# - If it’s at least N, I retrieve the salary at index N-1 (because indexing starts from 0).
# - If not, I assign None since there’s no Nth highest salary.
# I handle invalid input (N < 1) upfront by returning None.
# Finally, I wrap the result in a DataFrame with the required column name format and return it.
