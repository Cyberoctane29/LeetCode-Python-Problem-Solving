# Problem 184: Department Highest Salary
# Difficulty: Medium

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
# id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
# Each row of this table indicates the ID of a department and its name.

# Problem Statement:
# Write a function to find employees who have the highest salary in each of the departments.
# Return the result table in any order.

# Solution

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # I merge the Employee and Department tables on departmentId and id
    merged_df = pd.merge(
        employee, department,
        how='left',
        left_on='departmentId',
        right_on='id',
        suffixes=('_employee', '_department')
    )
    
    # I compute the maximum salary for each department using groupby and transform
    temp_series = merged_df.groupby('name_department')['salary'].transform('max')
    
    # I filter the rows where an employee's salary matches the department's maximum salary
    result_df = merged_df.loc[
        merged_df['salary'] == temp_series,
        ['name_department', 'name_employee', 'salary']
    ].rename(columns={
        'name_department': 'Department',
        'name_employee': 'Employee',
        'salary': 'Salary'
    })
    
    # I return the final result DataFrame
    return result_df

# Intuition:
# I need to identify the employee(s) with the highest salary in each department.
# To achieve this, I will merge both tables, compute the maximum salary per department, and select employees matching this value.

# Explanation:
# I start by merging the Employee and Department tables using a left join on the department IDs.
# I use `groupby` on the department name and `transform('max')` to compute the maximum salary for each department.
# I then filter the merged DataFrame to retain rows where the employee's salary equals the department's maximum salary.
# I select the necessary columns and rename them to match the required output format.
# Finally, I return this result as a DataFrame.
