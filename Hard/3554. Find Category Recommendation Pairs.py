# Problem 3554: Find Category Recommendation Pairs
# Difficulty: Hard

# Table: ProductPurchases
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | product_id  | int  |
# | quantity    | int  |
# +-------------+------+
# (user_id, product_id) is the unique identifier for this table.
# Each row represents a purchase of a product by a user in a specific quantity.

# Table: ProductInfo
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | category    | varchar |
# | price       | decimal |
# +-------------+---------+
# product_id is the unique identifier for this table.
# Each row assigns a category and price to a product.

# Problem Statement:
# Write a function to find all category pairs (where category1 < category2) such that:
# - At least 3 unique users purchased from both categories.
# Return the reportable category pairs and their customer_count, ordered by:
# 1. customer_count (descending),
# 2. category1 (ascending lexicographically),
# 3. category2 (ascending lexicographically).

# Solution

import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # I merge the purchase and product info to associate each purchase with its category
    merged_df = pd.merge(product_purchases, product_info, how='left', on='product_id')
    
    # I extract only the relevant columns: user and category
    temp_df = merged_df[['user_id', 'product_id', 'category']]
    
    # I self-join the dataset to find category pairs for the same user
    merged_df1 = temp_df.merge(temp_df, how='cross', suffixes=['1', '2'])
    
    # I filter rows where it's the same user and category1 < category2 to avoid duplicates and symmetric pairs
    temp_df1 = merged_df1.loc[
        (merged_df1['user_id1'] == merged_df1['user_id2']) &
        (merged_df1['category1'] < merged_df1['category2'])
    ]
    
    # I group by category pairs and count unique users
    result_df = temp_df1.groupby(['category1', 'category2'], as_index=False).agg(
        customer_count=('user_id1', 'nunique')
    )
    
    # I filter for category pairs with at least 3 customers
    result_df = result_df.loc[result_df['customer_count'] >= 3]
    
    # I sort as required by customer_count desc, category1 asc, category2 asc
    return result_df.sort_values(by=['customer_count', 'category1', 'category2'], ascending=[False, True, True])

# Intuition:
# I want to find category pairs that are co-purchased by at least 3 users.
# To do this, I treat each user as a source of potential category combinations,
# and then count how many users appear in each (category1, category2) pair.

# Explanation:
# I first merge the product purchase and product info tables to link product_id to its category.
# Then I reduce the data to just user_id and category to simplify the join.
# I perform a cross-join (self-merge) to get all category combinations per user.
# To avoid counting duplicate or reversed pairs (like A-B and B-A), I only keep pairs where category1 < category2.
# I group the resulting pairs by category1 and category2 and count the number of unique users per pair.
# Only those category pairs with at least 3 users are kept.
# Finally, I sort by the required order and return the cleaned result.
