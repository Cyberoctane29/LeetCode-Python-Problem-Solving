# Problem 176: Second Highest Salary
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
# Write a function to find the second highest distinct salary from the Employee table.
# If there is no second highest salary, return null (None in Pandas).

# Solution

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # I extract the unique salary values and sort them in descending order
    result_df = pd.Series(employee['salary'].unique()).sort_values(ascending=False)
    
    # I check if there is more than one distinct salary
    if len(result_df) > 1:
        # If so, I pick the second highest salary
        second_highest = result_df.iloc[1]
    else:
        # Otherwise, I set the result to None
        second_highest = None

    # I return the result as a DataFrame with the required column name
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})

# Intuition:
# I need to find the second largest unique salary from the Employee table.
# To do this, I first extract the unique salary values, then sort them in descending order.
# If at least two unique salaries exist, I select the second one. Otherwise, I return None.

# Explanation:
# I use the unique() method on the salary column to get distinct salaries.
# I convert this into a Pandas Series and sort it in descending order.
# I check the length of this sorted Series:
# - If it’s greater than 1, I retrieve the salary at index 1 (second highest).
# - If not, I assign None to indicate there’s no second highest salary.
# Finally, I wrap this value inside a DataFrame with the column name 'SecondHighestSalary' and return it.
