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
# product_id is the primary key (column with unique values) for this table.

# Table: Orders
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# This table may have duplicate rows.
# product_id is a foreign key (reference column) to the Products table.
# unit is the number of products ordered in order_date.

# Problem Statement:
# Write a function to get the names of products that have at least 100 units ordered in February 2020 and their amount.
# Return the result table in any order.

# Solution

import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I convert the 'order_date' column to datetime so I can filter it properly
    orders['order_date']=pd.to_datetime(orders['order_date'])
    
    # I filter the orders to only include records from February 2020
    filtered_df=orders.loc[(orders['order_date']>='2020-02-01')&((orders['order_date']<='2020-02-28')|(orders['order_date']<='2020-02-29')),:]
    
    # I group the filtered orders by product_id, sum the units, and immediately filter for those with 100+ units
    temp_df=filtered_df.groupby('product_id',as_index=False).agg({'unit':'sum'}).loc[(lambda x:x['unit']>=100),:]
    
    # I merge the filtered totals with the products table to get product names and select required columns
    merged_df1=pd.merge(temp_df,products,how='left',on='product_id')[['product_name','unit']]
    
    # Finally, I return the result DataFrame
    return merged_df1

# Intuition:
# I need to identify products that were ordered in February 2020 and had total units of at least 100.
# To do this, I will filter the Orders table for records from February 2020, group them by product_id, and compute the total units ordered for each product.
# After that, I will filter out products with fewer than 100 units ordered.
# Finally, I will merge these product IDs with the Products table to retrieve the product names along with the unit totals.

# Explanation:
# I start by converting the 'order_date' column to datetime format so that I can properly filter the dates.
# Next, I filter the Orders table to keep only those records where the order date falls within February 2020.
# Then, I group the filtered orders by product_id and calculate the total units ordered for each product in that period.
# I use a chained operation to immediately filter out any product with a total of less than 100 units.
# After that, I merge the filtered product totals with the Products table on product_id to get the corresponding product names.
# Lastly, I select only the product_name and unit columns for the final result and return it.
