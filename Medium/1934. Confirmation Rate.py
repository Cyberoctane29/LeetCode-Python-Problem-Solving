# Problem 1934: Confirmation Rate
# Difficulty: Medium

# Table: Signups
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | user_id        | int      |
# | time_stamp     | datetime |
# +----------------+----------+
# user_id is the column of unique values for this table.

# Table: Confirmations
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | user_id        | int      |
# | time_stamp     | datetime |
# | action         | ENUM     |
# +----------------+----------+
# (user_id, time_stamp) is the primary key for this table.
# action is an ENUM with values ('confirmed', 'timeout').

# Problem Statement:
# Write a function to calculate the confirmation rate of each user.
# The confirmation rate is the number of 'confirmed' messages divided by total confirmation requests made.
# If a user made no confirmation requests, their confirmation rate should be 0.
# Round the confirmation rate to two decimal places.

# Solution 1

import pandas as pd 

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # I group confirmations by user_id and compute confirmation rate as mean of (x == 'confirmed')
    temp_df = confirmations.groupby('user_id', as_index=False).agg(
        confirmation_rate=('action', lambda x: round((x == 'confirmed').mean(), 2))
    )
    
    # I merge with signups to ensure all users are included, filling NaNs with 0
    result_df = signups[['user_id']].merge(temp_df, on='user_id', how='left').fillna(0)

    # I return the final result
    return result_df

# Intuition:
# I need to compute the fraction of 'confirmed' actions for each user, even for those with no confirmations.

# Explanation:
# I group the Confirmations table by `user_id` and calculate the proportion of 'confirmed' actions using `.mean()`.
# Then, I merge this result with the Signups table to ensure all users are listed, replacing NaN confirmation rates (for users without confirmations) with 0.
# Finally, I return this merged DataFrame as the result.

# Solution 2

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # I group confirmations by user_id and compute confirmation rate as mean of (x == 'confirmed')
    temp_df = confirmations.groupby('user_id').agg(
        confirmation_rate=('action', lambda x: round((x == 'confirmed').mean(), 2))
    )

    # I reindex using the list of user_ids from signups to include users without confirmations
    result_df = temp_df.reindex(labels=signups['user_id'], fill_value=0).reset_index()

    # I return the final result
    return result_df

# Intuition:
# Similar to Solution 1 — but instead of merging, I reindex the grouped result directly based on the Signups table.

# Explanation:
# I compute the confirmation rate by grouping the Confirmations table by `user_id`.
# Then, I reindex this grouped result using the list of all user_ids from the Signups table.
# This ensures that users with no confirmations appear in the result, with their confirmation rate set to 0.
# Finally, I reset the index for a clean result and return it.
