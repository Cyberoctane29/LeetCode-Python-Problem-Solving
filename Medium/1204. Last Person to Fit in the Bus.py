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
# There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.
# Write a function to find the person_name of the last person that can fit on the bus without exceeding the weight limit.
# The test cases are generated such that the first person does not exceed the weight limit.
# Note that only one person can board the bus at any given turn.

# Solution

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # I sort the queue by 'turn' to ensure people board in the correct order
    queue = queue.sort_values(by='turn', ascending=True)
    
    # I calculate a running total of the cumulative weight as each person boards
    queue['total_weight'] = queue['weight'].cumsum()
    
    # I filter the queue to include only those whose cumulative weight does not exceed 1000
    # Then, I select the last person's name who can board and return it
    return queue.loc[queue['total_weight'] <= 1000, ['person_name']].tail(1)

# Intuition:
# I need to track the total weight on the bus as people board in turn order.
# By maintaining a cumulative sum and stopping before it exceeds 1000, I can identify the last person who fits.

# Explanation:
# I start by sorting the DataFrame by 'turn' so people board in order.
# I compute the cumulative sum of 'weight' using `cumsum()`.
# I then filter the records where the cumulative total does not exceed 1000.
# Finally, I pick the last entry from this filtered DataFrame using `.tail(1)` to get the name of the last person who can board.
