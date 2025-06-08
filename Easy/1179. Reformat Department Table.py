# Problem 1179: Reformat Department Table
# Difficulty: Easy

# Table: Department
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | revenue     | int     |
# | month       | varchar |
# +-------------+---------+
# (id, month) is the primary key in SQL.
# The month values are from ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].

# Problem Statement:
# Write a function to reformat the table so that each row represents a department id,
# and each month becomes a separate column holding its revenue.

# Solution

import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    # Define the correct chronological month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Pivot the table so months become columns, revenue becomes values
    result_df = department.pivot(index='id', columns='month', values='revenue')
    
    # Reorder the columns to match month_order
    result_df = result_df.reindex(columns=month_order)
    
    # Rename columns to match the required format
    result_df.columns = [f'{month}_Revenue' for month in result_df.columns]
    
    # Reset index to turn 'id' back into a regular column
    return result_df.reset_index()

# Intuition:
# - The problem requires reshaping the table from a long format, where each row represents a department-month revenue,
#   into a wide format, where each department has one row and a revenue column for each month.
# - I use the pivot function to turn 'month' values into columns, with 'revenue' as their values.
# - To maintain chronological order, I reorder the columns based on a predefined month sequence.
# - Lastly, I rename the columns to follow the required 'Month_Revenue' format and reset the index.

# Explanation:
# - The pivot operation restructures the DataFrame so that 'id' becomes the index, 'month' values become columns,
#   and 'revenue' fills the corresponding cells.
# - Since pivot doesn’t guarantee the desired month order, I explicitly reorder the columns with reindex.
# - I rename the month columns by appending '_Revenue' to each month name to match the expected output format.
# - Finally, resetting the index converts 'id' from an index back into a regular column.
