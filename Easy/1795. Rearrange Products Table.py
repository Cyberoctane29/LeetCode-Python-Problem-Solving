# Problem 1795: Rearrange Products Table
# Difficulty: Easy

# Table: Products
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store1      | int     |
# | store2      | int     |
# | store3      | int     |
# +-------------+---------+
# product_id is the primary key.
# Each row records a product's price in store1, store2, and store3.
# If a product is unavailable in a store, the price is null for that store.

# Problem Statement:
# Write a function to transform this wide-format table into a long-format table 
# with columns (product_id, store, price), excluding rows where price is null.

# Solution

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # I use pd.melt to reshape the table from wide to long format
    # id_vars keeps 'product_id' fixed, while other columns (store1, store2, store3) are melted into 'store' and 'price'
    result_df = pd.melt(products, id_vars='product_id', var_name='store', value_name='price')
    
    # I remove rows where price is null (i.e., product unavailable in that store)
    result_df = result_df.dropna(subset=['price'])
    
    # I return the final DataFrame
    return result_df

# Intuition:
# I need to convert the wide-format product price table into a long-format table.
# Pandas’ melt function is designed for this kind of unpivoting operation.
# After reshaping, I drop rows where the product isn’t available in a store (price is null).

# Explanation:
# I use pd.melt to reshape the table, keeping product_id as identifier.
# The columns store1, store2, store3 are unpivoted into a 'store' column, and their values go into a 'price' column.
# Then, I remove rows where the price is null because those represent unavailable products.
# Finally, I return the cleaned, reshaped DataFrame.
