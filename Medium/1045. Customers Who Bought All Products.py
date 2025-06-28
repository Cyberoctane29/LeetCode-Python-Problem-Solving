# Problem 1045: Customers Who Bought All Products
# Difficulty: Medium

# Table: Customer
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | customer_id | int     |
# | product_key | int     |
# +-------------+---------+
# This table may contain duplicate rows.
# customer_id is not NULL.
# product_key is a foreign key (reference column) to the Product table.

# Table: Product
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_key | int     |
# +-------------+---------+
# product_key is the primary key (column with unique values) for this table.

# Problem Statement:
# Write a function to report the customer IDs from the Customer table that bought all the products in the Product table.
# Return the result table in any order.

# Solution

import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # I count the total number of unique products from the Product table
    num_products = len(product)
    
    # I group the Customer table by customer_id and count how many unique products each customer bought
    temp_df = customer.groupby('customer_id', as_index=False).agg(
        num_times_bought=('product_key', 'nunique')
    )
    
    # I filter the customers who bought a number of unique products equal to the total number of products
    result_df = temp_df.loc[temp_df['num_times_bought'] == num_products, 'customer_id']
    
    # I return the result as a DataFrame containing only the qualifying customer IDs
    return pd.DataFrame(result_df)

# Intuition:
# I need to identify customers who bought every available product at least once.
# I will count the total number of unique products, then check for each customer how many unique products they bought, and select those matching the total.

# Explanation:
# I start by finding the total number of unique products using `len()` on the Product table.
# Then, I group the Customer table by 'customer_id' and compute how many unique products each customer bought using `nunique()`.
# I filter this result to retain only those customers whose count equals the total number of products.
# Finally, I extract and return their 'customer_id' in a new DataFrame.
