# Problem 1890: The Latest Login in 2020
# Difficulty: Easy

# Table: Logins
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | user_id        | int      |
# | time_stamp     | datetime |
# +----------------+----------+
# (user_id, time_stamp) is the primary key.
# Each row contains the login timestamp of a user.

# Problem Statement:
# Write a function to report the latest login for all users in the year 2020.
# Exclude users who did not log in during 2020.

# Solution

import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    # I filter the logins to include only those records where the login year is 2020
    filtered_df = logins[logins['time_stamp'].dt.year == 2020]
    
    # I group the filtered records by user_id and take the maximum timestamp for each user
    result_df = filtered_df.groupby('user_id', as_index=False).agg(last_stamp=('time_stamp', 'max'))
    
    # I return the final result
    return result_df

# Intuition:
# I need to find the latest login timestamp for each user within the year 2020.
# First, I’ll filter the logins for entries within 2020.
# Then, I’ll group by user_id and pick the maximum timestamp for each.

# Explanation:
# I use the dt accessor to extract the year from the 'time_stamp' column and keep only rows for 2020.
# Then, I group the filtered DataFrame by user_id.
# I aggregate by taking the maximum of 'time_stamp' to find the latest login per user.
# Finally, I return the result DataFrame containing user_id and their latest login timestamp.
