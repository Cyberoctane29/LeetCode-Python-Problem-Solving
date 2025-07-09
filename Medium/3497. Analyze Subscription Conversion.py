# Problem 3497: Analyze Subscription Conversion
# Difficulty: Medium

# Table: UserActivity
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | user_id          | int     |
# | activity_date    | date    |
# | activity_type    | varchar |
# | activity_duration| int     |
# +------------------+---------+
# (user_id, activity_date, activity_type) is the unique key.

# Problem Statement:
# Write a function to:
# - Identify users who converted from free trial to paid subscription
# - Calculate each user's average activity duration during free trial (rounded to 2 decimals)
# - Calculate each user's average activity duration during paid subscription (rounded to 2 decimals)
# Return the result ordered by user_id ascending.

# Solution 1

import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    # I keep only users who have at least one 'paid' activity
    temp_df = user_activity.loc[(user_activity['user_id'].isin(user_activity[user_activity['activity_type'] == 'paid']['user_id']))]

    # I compute trial and paid average durations for each such user
    result_df = temp_df.groupby('user_id', as_index=False).apply(
        lambda x: pd.Series({
            'trial_avg_duration': ((x.loc[x['activity_type'] == 'free_trial', 'activity_duration'].mean()) + 1e-8).round(2),
            'paid_avg_duration':  ((x.loc[x['activity_type'] == 'paid', 'activity_duration'].mean()) + 1e-8).round(2)
        })
    )

    # I return result ordered by user_id
    return result_df.sort_values(by='user_id')

# Intuition:
# I first identify users who converted by having a 'paid' activity record.
# Then for each such user, I compute average activity duration during both free trial and paid periods.

# Explanation:
# I use .isin() to filter users having at least one 'paid' activity.
# Then I group by user_id and compute the mean activity_duration separately for 'free_trial' and 'paid' using a lambda inside apply.
# 1e-8 is added to safely avoid NaN before rounding.
# The result is sorted by user_id ascending.

# Solution 2

import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    # I filter groups where at least one 'paid' activity exists
    temp_df = user_activity.groupby('user_id').filter(lambda x: (x['activity_type'] == 'paid').any())

    # I compute trial and paid average durations for each user
    result_df = temp_df.groupby('user_id', as_index=False).apply(
        lambda x: pd.Series({
            'trial_avg_duration': ((x.loc[x['activity_type'] == 'free_trial', 'activity_duration'].mean()) + 1e-8).round(2),
            'paid_avg_duration':  ((x.loc[x['activity_type'] == 'paid', 'activity_duration'].mean()) + 1e-8).round(2)
        })
    )

    # I return result ordered by user_id
    return result_df.sort_values(by='user_id')

# Intuition:
# Similar to Solution 1 — but here I first filter out entire groups (users) where no 'paid' activity is present.

# Explanation:
# I use groupby + filter to keep only users who have at least one 'paid' record.
# Then I group by user_id again and use apply + lambda to compute the average durations for 'free_trial' and 'paid'.
# Adding 1e-8 ensures no NaN errors before rounding.
# The result is returned sorted by user_id.
