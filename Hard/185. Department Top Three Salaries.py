# Problem 185: Department Top Three Salaries
# Difficulty: Hard

# Table: Employee
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | id           | int     |
# | name         | varchar |
# | salary       | int     |
# | departmentId | int     |
# +--------------+---------+
# id is the primary key (column with unique values) for this table.
# departmentId is a foreign key (reference column) of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

# Table: Department
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of a department and its name.

# Problem Statement:
# Write a function to find the employees who are high earners in each department.
# A high earner is defined as someone whose salary is among the top three unique salaries in their department.
# Return the result table in any order.

# Solution

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # I compute the salary rank within each department using dense ranking (no skipped ranks for ties)
    employee['rank'] = employee.groupby('departmentId', as_index=False)['salary'].rank(method='dense', ascending=False).astype(int)
    
    # I filter for top 3 ranked salaries within each department
    result_df = employee.loc[employee['rank'] <= 3, ] \
        .merge(department, how='left', left_on='departmentId', right_on='id', suffixes=['_employee', '_department']) \
        .rename(columns={
            'name_employee': 'Employee',
            'name_department': 'Department',
            'salary': 'Salary'
        })
    
    # I select and return the final required columns
    return result_df[['Department', 'Employee', 'Salary']]

# Intuition:
# I need to rank salaries within each department and retain employees whose rank falls within the top three.
# Using a dense rank ensures ties don't cause rank gaps, which is critical for fair inclusion of tied salaries.

# Explanation:
# I first group by 'departmentId' and apply `rank(method='dense', ascending=False)` to assign salary ranks within each department.
# The top 3 ranks are filtered using `employee['rank'] <= 3`.
# I merge this with the Department table to get department names and rename columns to match the output format.
# Finally, I return only the 'Department', 'Employee', and 'Salary' columns as required.
