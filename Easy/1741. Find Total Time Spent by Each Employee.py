# Problem 1741: Find Total Time Spent by Each Employee
# Difficulty: Easy

# Table: Employees
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | emp_id      | int  |
# | event_day   | date |
# | in_time     | int  |
# | out_time    | int  |
# +-------------+------+
# (emp_id, event_day, in_time) is the primary key for this table.
# This table tracks employees' entry and exit times from the office.
# Multiple entries per employee per day are possible. 
# The time spent in office for each entry is out_time - in_time.

# Problem Statement:
# Write a function to compute the total time spent in the office by each employee per day.
# Return the result table in any order with columns: day, emp_id, total_time.

# Solution

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # I group the data by emp_id and event_day
    # For each group, I compute total_time as the sum of (out_time - in_time) for that employee on that day
    result_df = employees.groupby(['emp_id','event_day'], as_index=False).apply(
        lambda x: pd.Series({'total_time': (x['out_time'] - x['in_time']).sum()})
    ).rename(columns={'event_day':'day'})  # I rename event_day to day as required

    # I select and return the final result columns in order: day, emp_id, total_time
    return result_df[['day','emp_id','total_time']]

# Intuition:
# I need to calculate the total minutes spent in the office by each employee on each day.
# Since employees can have multiple entries per day, I group the records by emp_id and event_day.
# Then, I sum up the duration (out_time - in_time) for each of these groups.

# Explanation:
# I group the Employees DataFrame by emp_id and event_day.
# I apply a lambda function to each group, calculating the total time spent by subtracting in_time from out_time for each record, then summing the result.
# I rename the event_day column to day as required by the problem statement.
# Finally, I select and order the required columns: day, emp_id, and total_time, and return the result.
