# Problem 610: Triangle Judgement
# Difficulty: Easy

# Table: Triangle
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# In SQL, (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.

# Problem Statement:
# Report for every three line segments whether they can form a triangle.
# Return the result table in any order.

# Solution

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    results = []  # list to store 'Yes' or 'No' for each row
    
    # iterate through each row as (x, y, z)
    for x, y, z in triangle.to_numpy():
        # apply triangle inequality theorem check
        if (x + y > z) & (y + z > x) & (x + z > y):
            results.append('Yes')  # if all conditions hold, it's a triangle
        else:
            results.append('No')  # otherwise, it's not a triangle
    
    # assign the results list as a new column 'triangle' to the dataframe
    triangle['triangle'] = results
    
    # return the updated dataframe
    return triangle

# Intuition:
# - I need to check if three line segments can form a triangle using the triangle inequality theorem.
# - According to this theorem, for any three sides to form a triangle, the sum of any two sides must be greater than the third side.
# - I iterate through each row of the dataframe and apply this check.

# Explanation:
# - I convert the dataframe to a NumPy array for efficient iteration.
# - For each triplet (x, y, z), I check if all three triangle inequality conditions hold.
# - If they do, I append 'Yes' to a results list; otherwise, 'No'.
# - I assign the results list as a new column called 'triangle' in the original dataframe and return it.
