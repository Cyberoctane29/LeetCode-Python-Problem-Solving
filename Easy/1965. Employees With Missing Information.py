# Problem 1965: Employees With Missing Information
# Difficulty: Easy

# Table: Employees
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row contains the name of an employee.

# Table: Salaries
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | salary      | int     |
# +-------------+---------+
# employee_id is the column with unique values for this table.
# Each row contains the salary of an employee.

# Problem Statement:
# Write a function to report the IDs of all the employees with missing information.
# Information is considered missing if either the employee's name is missing or their salary is missing.
# Return the result ordered by employee_id in ascending order.

# Solution

import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    # I merge the Employees and Salaries tables on employee_id using an outer join to retain all records
    merged_df = pd.merge(employees, salaries, how='outer', on='employee_id')
    
    # I filter the merged result to keep only the records where either 'name' or 'salary' is null
    result_df = merged_df.loc[(merged_df['name'].isna()) | (merged_df['salary'].isna()), ['employee_id']]
    
    # I return the final result
    return result_df

# Intuition:
# I need to identify employees who have missing information in either the Employees or Salaries table.
# To do this, I’ll perform an outer merge to retain all records and then filter for rows with null values in either the 'name' or 'salary' column.

# Explanation:
# I merge the Employees and Salaries tables using an outer join on employee_id so that no record is lost.
# Then, I use loc with a condition to filter rows where either 'name' or 'salary' is missing (null).
# I select only the 'employee_id' column for the final output.
# Finally, I return the filtered DataFrame.
