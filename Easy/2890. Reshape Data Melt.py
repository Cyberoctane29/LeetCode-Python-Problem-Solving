# Problem 2890: Reshape Data: Melt
# Difficulty: Easy

# Table: report
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | product     | object |
# | quarter_1   | int    |
# | quarter_2   | int    |
# | quarter_3   | int    |
# | quarter_4   | int    |
# +-------------+--------+

# Problem Statement:
# Write a function to reshape the `report` DataFrame so that each row represents 
# sales data for a product in a specific quarter.

# Solution

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    answer = report.melt(id_vars='product', var_name='quarter', value_name='sales')
    return answer

# Intuition:
# - The data needs to be converted from a wide format (where each quarter is a column) 
#   to a long format (where each row represents a product and its sales in a specific quarter).
# - I use the `melt()` function to transform the DataFrame.

# Explanation:
# - `report.melt(id_vars='product', var_name='quarter', value_name='sales')` reshapes 
#   the DataFrame by keeping `product` as an identifier column.
# - The `quarter_*` columns are transformed into rows, with the column names becoming values 
#   in the new `quarter` column, and their respective sales data moved under `sales`.
# - The function returns a new DataFrame where each row represents a product's sales 
#   for a specific quarter.
