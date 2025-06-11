# Problem 1327: List the Products Ordered in a Period
# Difficulty: Easy

# Table: Products
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | product_id       | int     |
# | product_name     | varchar |
# | product_category | varchar |
# +------------------+---------+
# product_id is the primary key.

# Table: Orders
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# This table may have duplicate rows.
# product_id is a foreign key referencing Products.product_id.
# unit is the number of products ordered on order_date.

# Problem Statement:
# Write a function to get the names of products that have at least 100 units ordered in February 2020 and their total ordered amount.
# Return the result table in any order.

# Solution

import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I convert the 'order_date' column to datetime to allow date filtering
    orders['order_date'] = pd.to_datetime(orders['order_date'])

    # I filter the Orders table to only include orders from February 2020
    filtered_df = orders.loc[(orders['order_date'] >= '2020-02-01') & (orders['order_date'] <= '2020-02-29'), :]

    # I group the filtered orders by product_id and calculate the total units ordered for each product
    temp_df = filtered_df.groupby('product_id', as_index=False).agg({'unit': 'sum'})

    # I filter the grouped result to retain only those products where total units >= 100
    temp_df = temp_df.loc[temp_df['unit'] >= 100, :]

    # I merge the filtered results with the Products table to get product names
    merged_df1 = pd.merge(temp_df, products, how='left', on='product_id')[['product_name', 'unit']]

    # Finally, I return the result DataFrame
    return merged_df1


# Intuition:
# I need to identify products that were ordered in a specific month and check if the total ordered units for each product meet a threshold.
# By filtering the Orders table for February 2020, grouping by product_id to sum up the units, and then joining with the Products table, I can get the product names and their total order amounts.
# Any product with 100 or more units ordered in the period should be included in the result.

# Explanation:
# I start by converting the 'order_date' column in the Orders table to datetime format for easy date comparison.
# I then filter the Orders table to only include orders where the order_date falls in February 2020.
# Next, I group the filtered records by product_id and sum up the 'unit' column to get total units ordered for each product.
# I retain only those products where the total ordered units are 100 or more.
# I merge this result with the Products table to get the product names associated with the product_ids.
# Finally, I select the 'product_name' and 'unit' columns for the output.
