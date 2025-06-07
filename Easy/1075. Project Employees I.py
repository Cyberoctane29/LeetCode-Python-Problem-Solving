# Problem 1075: Project Employees I
# Difficulty: Easy

# Table: Project
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# (project_id, employee_id) is the primary key of this table.
# employee_id is a foreign key to Employee table.
# Each row of this table indicates that the employee with employee_id is working on the project with project_id.

# Table: Employee
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | experience_years | int     |
# +------------------+---------+
# employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
# Each row of this table contains information about one employee.

# Problem Statement:
# Write a function that reports the average experience years of all employees per project.
# The average should be rounded to 2 decimal places.
# Return the result with columns 'project_id' and 'average_years'.


# Solution 1

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # I merge the project and employee tables on 'employee_id' to bring in experience years
    # Then I group by 'project_id' and compute the mean of 'experience_years' using named aggregation
    # Finally, I return a DataFrame with 'project_id' and 'average_years' (unrounded)
    return (
        project
        .merge(employee, how='left', on='employee_id')[['project_id', 'experience_years']]
        .groupby('project_id', as_index=False)
        .agg(average_years=('experience_years', 'mean'))
    )

# Intuition for Solution 1:
# - I want to find the average experience for employees working on each project.
# - I merge the project and employee tables on employee_id to get the experience years associated with each project.
# - Then, I group by project_id and use `.agg()` with named aggregation to compute the mean experience.
# - This gives me a DataFrame with project_id and the average experience (unrounded).

# Explanation for Solution 1:
# - The merge ensures that I align employee experience to their projects.
# - Grouping by project_id collects all employees of each project.
# - Using `.agg()` with named aggregation returns the average experience in a clean column called 'average_years'.
# - The average is not rounded here, so it may contain many decimal places.

# Solution 2

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # I merge the project and employee tables on 'employee_id' to bring in experience years
    # Then I group by 'project_id' and directly compute the mean of 'experience_years'
    # I reset the index and name the resulting column 'average_years'
    # Finally, I round the average values to 2 decimal places
    return (
        project
        .merge(employee, how='left', on='employee_id')[['project_id', 'experience_years']]
        .groupby('project_id')['experience_years']
        .mean()
        .reset_index(name='average_years')
        .round(2)
    )

# Intuition for Solution 2:
# - I do the same join to get the experience years for each project-employee pair.
# - Then, I group by project_id and directly call `.mean()` on the 'experience_years' series.
# - I reset the index to convert the result back to a DataFrame.
# - Finally, I round the average experience to 2 decimal places as required.

# Explanation for Solution 2:
# - This approach is more concise because it uses `.mean()` directly on the grouped series.
# - Resetting the index and naming the column 'average_years' makes the output similar to Solution 1.
# - Applying `.round(2)` explicitly rounds the average experience values to two decimals, fulfilling the problem requirement.
