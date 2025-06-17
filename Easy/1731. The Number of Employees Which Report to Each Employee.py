# Problem 1731: The Number of Employees Which Report to Each Employee
# Difficulty: Easy

# Table: Employees
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | reports_to  | int      |
# | age         | int      |
# +-------------+----------+
# employee_id is the unique identifier for each employee.
# This table contains employee information including the manager they report to.
# Some employees don’t report to anyone (reports_to is null).

# Problem Statement:
# Write a function to return the ids and names of all managers, 
# the number of employees reporting directly to them, 
# and the average age of those employees (rounded to the nearest integer).
# Return the result table ordered by employee_id.

# Solution

import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # I group the employees table by reports_to (manager) and compute:
    # 1. reports_count: number of direct reports
    # 2. average_age: average age of the direct reports, rounded to nearest integer (adding 1e-9 to handle edge rounding cases)
    temp_df = employees.groupby('reports_to', as_index=False).agg(
        reports_count=('employee_id', 'count'),
        average_age=('age', lambda x: round(x.mean() + 1e-9, 0))
    ).rename(columns={'reports_to': 'employee_id'})  # I rename 'reports_to' to 'employee_id' to match for merging

    # I merge this aggregated DataFrame with the original employees DataFrame on employee_id to get manager details
    result_df = pd.merge(employees, temp_df, how='inner', on='employee_id')

    # I select only the required columns and sort the result by employee_id in ascending order
    return result_df[['employee_id','name','reports_count','average_age']].sort_values(by='employee_id',ascending=True)

# Intuition:
# I need to find managers (employees with people reporting to them).
# I can group the Employees table by the reports_to field to compute:
# - the count of direct reports
# - the average age of those direct reports.
# Then, I merge these results back with the Employees table to fetch manager names.

# Explanation:
# I start by grouping the Employees DataFrame by reports_to to get the number of direct reports and average age.
# I rename the reports_to column to employee_id so it can be joined with the original employees DataFrame.
# I perform an inner merge to keep only those employee_ids who have at least one direct report.
# Then, I select the required columns: employee_id, name, reports_count, and average_age.
# I sort the final result by employee_id in ascending order before returning it.
