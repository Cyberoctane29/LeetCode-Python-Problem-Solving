# Problem 577: Employee Bonus
# Difficulty: Easy

# Table: Employee
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId is the unique identifier for each employee.
# Each row indicates the employee's ID, name, salary, and their supervisor's ID.

# Table: Bonus
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId is a foreign key referencing Employee.empId.
# Each row contains the employee's ID and their bonus amount.

# Problem Statement:
# Write a function to report the name and bonus amount of each employee with a bonus less than 1000.
# If the employee has no bonus record (null), include them as well.
# Return the result in any order.

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and bonus tables on 'empId' using a left join to keep all employees
    merged_emp_bon = employee.merge(bonus, how='left', on='empId')
    
    # Filter employees with bonus less than 1000 or with no bonus record (NaN)
    result = merged_emp_bon.loc[
        (merged_emp_bon['bonus'] < 1000) | (merged_emp_bon['bonus'].isnull()),
        ['name', 'bonus']
    ]
    return result

# Intuition:
# - I want to include all employees, even those without a bonus record, so I do a left join.
# - Then I filter for those whose bonus is less than 1000 or have no bonus assigned (null values).

# Explanation:
# - I merge the Employee table with the Bonus table on 'empId' using a left join.
# - This ensures employees without a bonus still appear with NaN in the bonus column.
# - Then I filter rows where 'bonus' < 1000 or where 'bonus' is null.
# - Finally, I select only the 'name' and 'bonus' columns for the output.
