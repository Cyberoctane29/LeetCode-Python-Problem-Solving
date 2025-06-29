# Problem 1158: Market Analysis I
# Difficulty: Medium

# Table: Users
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | join_date      | date    |
# | favorite_brand | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) of this table.
# This table has the info of the users of an online shopping website where users can sell and buy items.

# Table: Orders
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | item_id       | int     |
# | buyer_id      | int     |
# | seller_id     | int     |
# +---------------+---------+
# order_id is the primary key (column with unique values) of this table.
# item_id is a foreign key (reference column) to the Items table.
# buyer_id and seller_id are foreign keys to the Users table.

# Table: Items
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | item_id       | int     |
# | item_brand    | varchar |
# +---------------+---------+
# item_id is the primary key (column with unique values) for this table.

# Problem Statement:
# Write a function to find for each user, the join date and the number of orders they made as a buyer in 2019.
# Return the result table in any order.

# Solution

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # I filter the Orders table to include only orders made in 2019
    orders_2019 = orders.loc[(orders['order_date'].dt.year == 2019), ]
    
    # I group by buyer_id to count the number of orders made by each buyer in 2019
    temp_df = orders_2019.groupby('buyer_id', as_index=False).agg(
        orders_in_2019=('order_id', 'count')
    )
    
    # I merge the Users table with the aggregated order count table
    result_df = pd.merge(users, temp_df, how='left', left_on='user_id', right_on='buyer_id')
    
    # I replace NaN values with 0 for users who made no orders in 2019
    result_df['orders_in_2019'] = result_df['orders_in_2019'].fillna(0)
    
    # I select the necessary columns, rename 'user_id' to 'buyer_id', and return the final result
    return result_df[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id': 'buyer_id'})

# Intuition:
# I need to find how many orders each user placed as a buyer during 2019 and report it along with their join date.
# Filtering orders by year and joining this count back to the user details makes this straightforward.

# Explanation:
# I begin by filtering the Orders table to keep only rows where the order date falls in 2019.
# I then group the filtered data by 'buyer_id' and count how many orders each buyer made in 2019.
# This aggregated result is merged with the Users table using a left join to retain all users.
# Users who didn’t place any orders in 2019 will have NaN values in the 'orders_in_2019' column, which I replace with 0.
# Finally, I select the relevant columns, rename 'user_id' to 'buyer_id', and return the cleaned result.
