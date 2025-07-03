# Problem 1204: Last Person to Fit in the Bus
# Difficulty: Medium

# Table: Queue
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | person_id   | int     |
# | person_name | varchar |
# | weight      | int     |
# | turn        | int     |
# +-------------+---------+
# person_id column contains unique values.
# This table has the information about all people waiting for a bus.
# The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
# turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
# weight is the weight of the person in kilograms.

# Problem Statement:
# Write a function to find the person_name of the last person that can fit on the bus without exceeding the weight limit.
# The bus has a weight limit of 1000 kilograms.
# The test cases are generated such that the first person does not exceed the weight limit.
# Only one person can board the bus at any given turn.

# Solution

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # I sort the queue based on 'turn' to maintain boarding order
    queue = queue.sort_values(by='turn', ascending=True)
    
    # I compute the cumulative sum of weights as people board
    queue['total_weight'] = queue['weight'].cumsum()
    
    # I select people who can fit without exceeding 1000 kg, and pick the last one’s 'person_name'
    return queue.loc[queue['total_weight'] <= 1000, ['person_name']].iloc[[-1]]

# Intuition:
# I need to track the running total of weights as people board in turn order.
# The last person whose boarding keeps the total within 1000 kg is the answer.

# Explanation:
# I first sort the queue by 'turn' to ensure people board in order.
# I then calculate the cumulative sum of weights as each person boards.
# I filter to keep only those whose cumulative weight doesn’t exceed 1000 kg.
# From this filtered list, I use `.iloc[[-1]]` to retrieve the last person to board within the limit.
# I return this result containing only the 'person_name' column.
