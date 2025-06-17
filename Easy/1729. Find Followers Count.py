# Problem 1729: Find Followers Count
# Difficulty: Easy

# Table: Followers
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | follower_id | int  |
# +-------------+------+
# (user_id, follower_id) is the primary key for this table.
# This table contains pairs of user IDs and their corresponding follower IDs in a social media app.

# Problem Statement:
# Write a function to, for each user, return the number of followers they have.
# Return the result table ordered by user_id in ascending order.

# Solution

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    # I group the followers table by user_id and count the number of follower_id for each user
    result_df=followers.groupby('user_id',as_index=False).agg(followers_count=('follower_id','count')) \
                       .sort_values(by='user_id',ascending=True)  # I sort the result by user_id in ascending order
    
    # I return the final result
    return result_df

# Intuition:
# I need to count how many followers each user has.
# To achieve this, I will group the followers table by user_id and count how many follower_id entries exist for each.

# Explanation:
# I group the followers DataFrame by user_id.
# For each group, I count the number of follower_id values using the count() function.
# I name the resulting column followers_count.
# I then sort the resulting DataFrame by user_id in ascending order.
# Finally, I return this sorted DataFrame as the result.
