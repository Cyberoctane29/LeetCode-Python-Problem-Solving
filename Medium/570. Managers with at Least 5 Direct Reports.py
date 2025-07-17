# Problem 570: Managers with at Least 5 Direct Reports
# Difficulty: Medium

# Table: Employee

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.

# Problem Statement:
# Write a function to find managers with at least five direct reports.
# Return the result table in any order.

# Solution

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # I group by 'managerId' and count how many employees report to each manager
    temp_df = employee.groupby('managerId', as_index=False).agg(count=('managerId', 'count'))
    
    # I filter to only those managers who have 5 or more direct reports
    temp_df = temp_df.loc[(temp_df['count'] >= 5), 'managerId']
    
    # I select names of employees whose id matches the filtered managerIds
    result_df = employee.loc[employee['id'].isin(temp_df), 'name']
    
    # I return the result as a DataFrame with column name 'name'
    return pd.DataFrame({'name': result_df})

# Intuition:
# I need to find which managers have five or more employees reporting to them directly.
# This means counting how often each managerId appears in the employee table,
# then looking up those managerIds in the main table to get their names.

# Explanation:
# First, I group the table by 'managerId' and count the number of occurrences — this gives me the number of direct reports.
# Then, I filter this grouped result to retain only managerIds that have at least 5 reports.
# I use `isin()` to match these managerIds against the 'id' column in the original employee table — 
# since 'id' is the employee's own ID, I can retrieve the names of managers from it.
# Finally, I return just their names in a new DataFrame.
