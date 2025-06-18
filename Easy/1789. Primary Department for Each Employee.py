# Problem 1789: Primary Department for Each Employee
# Difficulty: Easy

# Table: Employee
# +---------------+---------+
# | Column Name   |  Type   |
# +---------------+---------+
# | employee_id   | int     |
# | department_id | int     |
# | primary_flag  | varchar |
# +---------------+---------+
# (employee_id, department_id) is the primary key for this table.
# Employees can belong to multiple departments. Each employee has a 'Y' for their primary department.
# If an employee belongs to only one department, their primary_flag is 'N'.

# Problem Statement:
# Write a function to return each employee’s primary department.
# If an employee has only one department, return that department.
# Otherwise, return the department where primary_flag is 'Y'.

# Solution

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # I group the data by employee_id
    # For each group (employee), I select the department_id where either:
    # - The employee belongs to only one department (x.shape[0] == 1)
    # - Or the primary_flag is 'Y'
    # Since both conditions are exclusive per group, I safely take the first matching department_id
    result_df = employee.groupby('employee_id', as_index=False).apply(
        lambda x: pd.Series({
            'department_id': x.loc[(x.shape[0] == 1) | (x['primary_flag'] == 'Y'), 'department_id'].values[0]
        })
    )

    # I return the final result
    return result_df

# Intuition:
# I need to get the primary department for each employee.
# If the employee is in only one department, that’s their primary department.
# Otherwise, I pick the department where primary_flag is 'Y'.

# Explanation:
# I group the Employee DataFrame by employee_id.
# For each group:
# - If there’s only one record, I pick that department.
# - If multiple records exist, I select the one where primary_flag is 'Y'.
# I use a lambda function with pd.Series to format the result with the required department_id.
# Finally, I return the result as a DataFrame containing employee_id and department_id.
