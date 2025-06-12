# Problem 1378: Replace Employee ID With The Unique Identifier
# Difficulty: Easy

# Table: Employees
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the id and the name of an employee in a company.

# Table: EmployeeUNI
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | unique_id     | int     |
# +---------------+---------+
# (id, unique_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the id and the corresponding unique id of an employee in the company.

# Problem Statement:
# Write a function to show the unique ID of each user.
# If a user does not have a unique ID, just show null.
# Return the result table in any order.

# Solution

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # I perform a left join between Employees and EmployeeUNI on 'id'
    return pd.merge(employees,employee_uni,how='left',on='id')[['unique_id','name']]

# Intuition:
# I need to display the unique_id associated with each employee based on their id.
# If an employee doesn’t have a corresponding unique_id in the EmployeeUNI table, it should appear as null in the final result.
# To achieve this, I will perform a left join between the Employees and EmployeeUNI tables on the 'id' column.

# Explanation:
# I start by merging the Employees table with the EmployeeUNI table using a left join on the 'id' column.
# This ensures that every employee from the Employees table is retained in the result, and if a matching unique_id exists in EmployeeUNI, it is added.
# If no match is found, the unique_id for that employee will be null.
# Finally, I select and return only the 'unique_id' and 'name' columns in the required order.
