# Problem 180: Consecutive Numbers
# Difficulty: Medium

# Table: Logs
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# id is the primary key and auto-increments from 1.

# Problem Statement:
# Write a function to find all numbers that appear at least three times consecutively in the table.
# Return the result as a table with a single column `ConsecutiveNums` listing those numbers.

# Solution

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # I create an empty set to store numbers that appear at least 3 times consecutively
    result_set = set()
    
    # I define the window size as 3
    k = 3  
    
    # I loop through the logs DataFrame using a sliding window of size 3
    for i in range(0, len(logs) - k + 1):
        # I extract a window of 3 consecutive numbers
        window = logs['num'].iloc[i:i+k]
        
        # If all numbers in the window are the same, I add the number to the result set
        if len(window.unique()) == 1:
            result_set.add(window.iloc[0])
    
    # I return the final result as a DataFrame
    return pd.DataFrame({'ConsecutiveNums': list(result_set)})

# Intuition:
# I need to identify numbers that repeat consecutively at least 3 times.
# I will use a sliding window of size 3 and check whether all elements in the window are identical.
# If they are, I'll record the number.

# Explanation:
# I initialize an empty set to store the qualifying numbers.
# I iterate through the DataFrame using a loop to define a sliding window of 3 consecutive values from the 'num' column.
# I check if all values within the window are identical using len(window.unique()) == 1.
# If so, I add the number to the result set.
# After the loop, I convert the set into a DataFrame with the required column name and return it.
