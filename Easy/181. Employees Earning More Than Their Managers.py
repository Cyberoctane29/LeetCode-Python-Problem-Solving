# Problem 181: Employees Earning More Than Their Managers
# Difficulty: Easy

# Table: Employee
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

# Problem Statement:
# Write a function to find the employees who earn more than their managers.
# Return the result table in any order.

# Solution

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    temp = employee.merge(
        employee[['id', 'salary']],  
        left_on='managerId',
        right_on='id',
        how='left',
        suffixes=('', '_manager')
    )
    answer = temp.loc[temp['salary'] > temp['salary_manager'], ['name']].rename(columns={'name': 'Employee'})
    
    return answer

# Intuition:
# - I need to compare each employee's salary with their manager's salary.
# - Since both employees and managers exist in the same table, I perform a self-join on 'managerId' and 'id'.
# - I then filter for employees whose salary is greater than their manager's.

# Explanation:
# - I use the `.merge()` function to join the Employee table with itself on 'managerId' and 'id'.
# - The manager's salary is retrieved in a new column 'salary_manager'.
# - I filter rows where the employee's salary is greater than the manager's salary.
# - Finally, I select only the 'name' column and rename it to 'Employee' for the final output.
