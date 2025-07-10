# Problem 3521: Find Product Recommendation Pairs
# Difficulty: Medium

# Table: ProductPurchases
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | product_id  | int  |
# | quantity    | int  |
# +-------------+------+
# (user_id, product_id) is the unique key.

# Table: ProductInfo
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | category    | varchar |
# | price       | decimal |
# +-------------+---------+
# product_id is the primary key.

# Problem Statement:
# Write a function to:
# - Identify product pairs (product1_id < product2_id) frequently purchased together by the same customers
# - For each pair, count how many customers purchased both
# - Keep pairs purchased together by at least 3 customers
# Return the result ordered by customer_count (descending), product1_id, then product2_id.

# Solution

import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # I create a cross join of all possible product pairs where product1 < product2
    merged_df = pd.merge(product_info, product_info, how='cross').loc[
        (lambda x: x['product_id_x'] < x['product_id_y'])
    ].drop(columns=['price_x', 'price_y'])

    # Initialize count of customers who bought both products
    merged_df['pair_count'] = 0

    # I group each user's purchases into a set
    user_groups = product_purchases.groupby('user_id')['product_id'].apply(set)

    # For each user and each product pair, I check if both products exist in their purchase set
    for products in user_groups:
        for idx, row in merged_df.iterrows():
            if (row['product_id_x'] in products) & (row['product_id_y'] in products):
                merged_df.loc[idx, 'pair_count'] += 1

    # I filter pairs with at least 3 customers
    result_df = merged_df[merged_df['pair_count'] >= 3].rename(
        columns={
            'product_id_x': 'product1_id',
            'category_x': 'product1_category',
            'product_id_y': 'product2_id',
            'category_y': 'product2_category',
            'pair_count': 'customer_count'
        })

    # I select the required columns and sort as per instruction
    return result_df[['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']].sort_values(
        by=['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True]
    )

# Intuition:
# I need to find all product pairs (product1 < product2) and count how many customers purchased both.
# If at least 3 customers did, I include the pair in the final result.

# Explanation:
# - I use a cross join on ProductInfo to generate all possible unique product pairs.
# - I group purchases by user into a set.
# - For each user, I check whether both products in a pair exist in their purchase set and increment the pair count.
# - After counting, I filter out pairs purchased by fewer than 3 customers.
# - Finally, I sort by customer_count (desc), then product1_id and product2_id (asc) as required.
