# Problem 1407: Top Travellers
# Difficulty: Easy

# Table: Users
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the column with unique values for this table.
# name is the name of the user.

# Table: Rides
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | user_id       | int     |
# | distance      | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# user_id is the id of the user who traveled the distance "distance".

# Problem Statement:
# Write a function to report the distance traveled by each user.
# Return the result table ordered by travelled_distance in descending order.
# If two or more users traveled the same distance, order them by their name in ascending order.

# Solution

import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # I group the Rides table by user_id and calculate the total travelled_distance for each user
    rides_tempdf=rides.groupby('user_id', as_index=False).agg(travelled_distance=('distance','sum'))

    # I merge the total distances with the Users table using a left join
    merged_df=pd.merge(users,rides_tempdf,how='left',left_on='id',right_on='user_id')

    # I replace NaN values in travelled_distance with 0 for users with no rides
    merged_df['travelled_distance']=merged_df['travelled_distance'].fillna(0)

    # I sort the final result by travelled_distance in descending order, then by name in ascending order
    return merged_df.sort_values(by=['travelled_distance','name'],ascending=[False,True])[['name','travelled_distance']]

# Intuition:
# I need to compute the total distance traveled by each user.
# To do this, I will group the Rides table by user_id and sum the distance for each user.
# Then, I will merge these totals with the Users table so that every user is included.
# Users with no rides should have a travelled_distance of 0.
# Finally, I will sort the results by travelled_distance in descending order and by name in ascending order to handle ties.

# Explanation:
# I start by grouping the Rides table by user_id and summing the distance values to get the total travelled_distance for each user.
# Next, I merge this result with the Users table on the 'id' column using a left join so that all users appear in the final result.
# I replace any missing travelled_distance values (for users who didn't travel at all) with 0.
# Lastly, I sort the result by travelled_distance in descending order and, for ties, by name in ascending order.
# I select and return only the 'name' and 'travelled_distance' columns as required.
