# Problem 1757: Recyclable and Low Fat Products
# Difficulty: Easy

# Table: Products
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | low_fats    | enum    |
# | recyclable  | enum    |
# +-------------+---------+
# product_id is the primary key (column with unique values) for this table.
# low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
# recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

# Problem Statement:
# Write a function to find the ids of products that are both low fat and recyclable.
# Return the result table in any order.

# Solution

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), ['product_id']]

# Intuition:
# - I need to filter out products that satisfy both conditions:
#   1. The product must be low fat (`low_fats == 'Y'`).
#   2. The product must be recyclable (`recyclable == 'Y'`).

# Explanation:
# - `products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]` filters rows that meet both conditions.
# - `[['product_id']]` ensures that only the `product_id` column is returned.
