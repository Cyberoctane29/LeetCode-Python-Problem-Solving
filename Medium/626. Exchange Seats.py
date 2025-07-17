# Problem 626: Exchange Seats
# Difficulty: Medium

# Table: Seat

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | student     | varchar |
# +-------------+---------+
# id is the primary key (unique value) column for this table.
# Each row of this table indicates the name and the ID of a student.
# The ID sequence always starts from 1 and increments continuously.

# Problem Statement:
# Write a function to swap the seat id of every two consecutive students.
# If the number of students is odd, the id of the last student is not swapped.
# Return the result table ordered by id in ascending order.

# Solution

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    result_df = seat.copy()
    
    # I loop through every pair of indices (0 and 1, 2 and 3, etc.)
    for i in range(0, len(seat) - 1, 2):
        # I swap the student names between the two adjacent rows
        result_df.loc[i, 'student'], result_df.loc[i + 1, 'student'] = seat.loc[i + 1, 'student'], seat.loc[i, 'student']
    
    # I return the DataFrame sorted by 'id'
    return result_df.sort_values(by='id')

# Intuition:
# I want to simulate the effect of swapping seats in pairs based on their order,
# without changing their original IDs.

# Explanation:
# I copy the DataFrame to avoid changing the original data.
# Since IDs start from 1 but Python is 0-indexed, I loop in steps of 2 starting from index 0.
# For each consecutive pair, I swap the student names.
# If the number of rows is odd, the last student is left untouched because the loop ends at len(seat) - 1.
# Finally, I sort by 'id' to keep the output consistent with the original order.
