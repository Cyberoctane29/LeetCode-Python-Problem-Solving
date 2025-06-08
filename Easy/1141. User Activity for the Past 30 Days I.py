# Problem 1141: User Activity for the Past 30 Days I
# Difficulty: Easy

# Table: Activity
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | session_id    | int     |
# | activity_date | date    |
# | activity_type | enum    |
# +---------------+---------+
# The activity_type column is an ENUM of ('open_session', 'end_session', 'scroll_down', 'send_message').
# This table may have duplicate rows.

# Problem Statement:
# Write a function to find the daily active user count for a 30-day period ending 2019-07-27 inclusively.
# A user is considered active on a given day if they performed any activity on that day.

# Solution

import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # I convert 'activity_date' to datetime format for filtering
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    
    # I calculate the start date for the 30-day period ending 2019-07-27
    start_date = pd.to_datetime('2019-07-27') - pd.DateOffset(days=29)
    
    # I group by 'activity_date' and count unique users for each day
    # Then rename 'activity_date' to 'day' and filter for dates within the desired range
    return (
        activity
        .groupby('activity_date', as_index=False)
        .agg(active_users=('user_id', 'nunique'))
        .rename(columns={'activity_date': 'day'})
        .loc[lambda x: (x['day'] >= start_date) & (x['day'] <= '2019-07-27'), :]
    )

# Intuition:
# - The task requires counting distinct active users for each day over the past 30 days from a given end date.
# - First, I convert 'activity_date' to datetime so I can perform date comparisons.
# - Then, I calculate the start date by subtracting 29 days from the end date.
# - I group the data by each day and count unique users, which directly gives me the daily active user count.
# - Lastly, I filter the results to keep only those within the required date window.

# Explanation:
# - Converting 'activity_date' to datetime ensures proper handling of date comparisons and filtering.
# - Grouping by 'activity_date' and using nunique on 'user_id' counts the number of distinct users active each day.
# - The start date is computed as 29 days before '2019-07-27' to cover the 30-day inclusive period.
# - The final filter keeps rows where 'day' lies within the inclusive window from the start date to '2019-07-27'.
# - Renaming 'activity_date' to 'day' aligns with the required result format.
