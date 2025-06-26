# Problem 602: Friend Requests II: Who Has the Most Friends
# Difficulty: Medium

# Table: RequestAccepted
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | requester_id   | int     |
# | accepter_id    | int     |
# | accept_date    | date    |
# +----------------+---------+
# (requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
# This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.

# Problem Statement:
# Write a function to find the person who has the most friends and the number of friends they have.
# The test cases are generated so that only one person will have the most friends.

# Solution

import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # I count the number of requests sent by each requester
    requester_counts = request_accepted.groupby('requester_id', as_index=False).agg(
        count=('requester_id', 'count')
    ).rename(columns={'requester_id': 'id'})
    
    # I count the number of requests accepted by each accepter
    accepter_counts = request_accepted.groupby('accepter_id', as_index=False).agg(
        count=('accepter_id', 'count')
    ).rename(columns={'accepter_id': 'id'})
    
    # I combine both counts into a single DataFrame
    combined_counts = pd.concat([requester_counts, accepter_counts])
    
    # I group by user ID and sum their total friend connections
    result_df = combined_counts.groupby('id', as_index=False).agg(num=('count', 'sum'))
    
    # I return the user with the highest number of friends
    return result_df.loc[result_df['num'] == result_df['num'].max(), ['id', 'num']]

# Intuition:
# I need to count the total number of friends each person has, considering both sent and received friend requests.
# By counting requests as both requester and accepter, and then combining these counts, I can identify the person with the highest total.

# Explanation:
# I first count how many times each user appears as a requester using `groupby` and `count()`, renaming the column to 'id'.
# I repeat the same for appearances as an accepter.
# I combine both results using `pd.concat()` to stack them vertically.
# I then group the combined DataFrame by 'id' and sum the counts to get the total number of connections for each user.
# Finally, I locate the user(s) whose total connections equal the maximum value and return their 'id' and total number of friends as 'num'.
