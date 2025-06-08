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
# I need to reformat the table so each row represents a department id,
# and each month becomes a separate column holding its revenue.

# Solution

import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    # I define the correct chronological month order to preserve it in the final output
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # I pivot the table so that each month becomes a separate column and the revenue values fill the cells
    result_df = department.pivot(index='id', columns='month', values='revenue')
    
    # I reorder the columns to match the correct month order
    result_df = result_df.reindex(columns=month_order)
    
    # I rename the columns by adding '_Revenue' to each month to match the expected format
    result_df.columns = [f'{month}_Revenue' for month in result_df.columns]
    
    # Finally, I reset the index so that 'id' turns back into a regular column instead of an index
    return result_df.reset_index()

# Intuition:
# I’m asked to reshape the table from a long format, where each row represents a department’s revenue in a month, 
# into a wide format, where each department has one row and a revenue column for every month.
# To achieve this, I use the pivot function to transform 'month' values into columns.
# Then, I reorder the columns to follow the correct calendar sequence.
# After that, I rename the columns to include '_Revenue' and reset the index to make 'id' a regular column.

# Explanation:
# First, I use pivot to restructure the DataFrame so that 'id' becomes the index, 'month' values become columns,
# and 'revenue' fills in the appropriate cells.
# Since the pivot result might not maintain the desired month order, I reorder the columns using reindex.
# Next, I rename all month columns by appending '_Revenue' to each one to match the expected naming convention.
# Lastly, I reset the index so that 'id' moves from the index position back into a regular column.
