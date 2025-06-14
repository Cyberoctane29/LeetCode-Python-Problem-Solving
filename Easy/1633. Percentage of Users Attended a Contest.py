# Problem 1633: Percentage of Users Attended a Contest
# Difficulty: Easy

# Table: Users
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | user_name   | varchar |
# +-------------+---------+
# user_id is the primary key (column with unique values) for this table.
# Each row of this table contains the name and the id of a user.

# Table: Register
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | contest_id  | int     |
# | user_id     | int     |
# +-------------+---------+
# (contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the id of a user and the contest they registered into.

# Problem Statement:
# Write a function to find the percentage of the users registered in each contest rounded to two decimals.
# Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # I get the total number of users
    user_cnt = users.shape[0]

    # I group the Register table by contest_id and calculate the percentage of users registered for each contest
    temp_df = register.groupby('contest_id', as_index=False).agg(
        percentage=('user_id', lambda x: round(((x.shape[0] / user_cnt) * 100), 2))
    )

    # I sort the result by percentage in descending order and by contest_id in ascending order
    result_df = temp_df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

    # I return the final result
    return result_df

# Intuition:
# I need to calculate the percentage of users registered in each contest relative to the total number of users.
# To do this, I will first get the total number of users.
# Then, I will group the Register table by contest_id and count the number of users per contest.
# After that, I will compute the percentage by dividing the count by the total number of users and multiplying by 100.
# Finally, I will sort the results as required.

# Explanation:
# I start by determining the total number of users from the Users table using the shape property.
# Next, I group the Register table by contest_id and use a lambda function to compute the percentage of total users registered for each contest.
# I round the percentage to two decimal places.
# Then, I sort the resulting DataFrame first by percentage in descending order and then by contest_id in ascending order.
# Lastly, I return the final DataFrame with contest_id and corresponding percentage.
