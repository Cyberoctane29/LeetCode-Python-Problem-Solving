# Problem 1873: Calculate Special Bonus
# Difficulty: Easy

# Table: Employees
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.

# Problem Statement:
# Write a function to calculate the bonus of each employee.
# The bonus of an employee is 100% of their salary if:
# - The employee ID is an odd number.
# - The employee's name does not start with the character 'M'.
# Otherwise, the bonus is 0.
# Return the result table ordered by employee_id.

# Solution 1:

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] % 2 != 0) & ~(employees['name'].str.startswith('M')), ['bonus']] = employees['salary']
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')

# Intuition:
# - We need to set the `bonus` column to 100% of the employee's salary if they meet the conditions.
# - We create a new column `bonus` initialized to 0 for all employees.
# - We use `.loc[]` to apply the condition:
#   - The employee ID should be odd (`employee_id % 2 != 0`).
#   - The employee’s name should **not** start with ‘M’ (`~employees['name'].str.startswith('M')`).
# - If both conditions are met, we assign the `salary` value to `bonus`.
# - Finally, we return only `employee_id` and `bonus`, sorted by `employee_id`.

# Explanation:
# - The approach modifies the DataFrame directly by adding a new `bonus` column.
# - The `.loc[]` method ensures the filtering and assignment are done efficiently in one step.
# - Sorting at the end ensures the correct output order.

# Solution 2:

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = [
        salary if (emp_id % 2 != 0 and not name.startswith('M')) else 0
        for emp_id, name, salary in zip(employees['employee_id'], employees['name'], employees['salary'])
    ]
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')

# Intuition:
# - We need to check each employee individually and determine their bonus.
# - We use a **list comprehension** to iterate over the three columns (`employee_id`, `name`, `salary`) at once.
# - For each row:
#   - If `employee_id` is odd **and** `name` does not start with 'M', set `bonus = salary`.
#   - Otherwise, set `bonus = 0`.

# Explanation:
# - We use `zip()` to iterate through multiple columns simultaneously.
# - The conditional logic inside the list comprehension makes it easy to construct the `bonus` list.
# - Since the list is created in one step, this approach is efficient and readable.
# - Finally, we create the `bonus` column and return the required columns sorted by `employee_id`.
