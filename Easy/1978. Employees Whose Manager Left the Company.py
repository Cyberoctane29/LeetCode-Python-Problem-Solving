# Problem 1978: Employees Whose Manager Left the Company
# Difficulty: Easy

# Table: Employees
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | manager_id  | int      |
# | salary      | int      |
# +-------------+----------+
# employee_id is the primary key for this table.
# This table contains information about employees, their salaries, and the IDs of their managers.
# Some employees do not have a manager (manager_id is null).

# Problem Statement:
# Write a function to find the IDs of employees whose salary is strictly less than $30000 and whose manager has left the company.
# When a manager leaves, their record is deleted from the Employees table, but the reporting employees retain the manager_id value.
# Return the result ordered by employee_id.

# Solution

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # I filter the employees with salary less than 30000
    filtered_df = employees[employees['salary'] < 30000]
    
    # I further filter for records where manager_id is not null and not present in employee_id column (manager left)
    result_df = filtered_df.loc[
        (filtered_df['manager_id'].notna()) & (~filtered_df['manager_id'].isin(employees['employee_id'])),
        ['employee_id']
    ]
    
    # I return the result sorted by employee_id
    return result_df.sort_values(by='employee_id')

# Intuition:
# I need to identify employees earning less than $30000 whose manager’s record is missing from the Employees table.
# To do this, I’ll filter those with salary under 30000, then check if their manager_id isn’t null and doesn’t exist in the employee_id column.

# Explanation:
# I start by filtering the Employees table for entries with salary less than 30000.
# Next, I check for employees whose manager_id is not null and whose manager_id is absent from the list of current employee_ids.
# This means their manager left the company.
# I select only the 'employee_id' column and sort the result by employee_id in ascending order.
# Finally, I return the resulting DataFrame.
