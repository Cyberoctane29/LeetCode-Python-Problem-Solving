# Problem 1084: Sales Analysis III
# Difficulty: Easy

# Table: Product
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# | unit_price   | int     |
# +--------------+---------+
# product_id is the primary key of this table.
# Each row indicates the name and price of each product.

# Table: Sales
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | seller_id   | int     |
# | product_id  | int     |
# | buyer_id    | int     |
# | sale_date   | date    |
# | quantity    | int     |
# | price       | int     |
# +-------------+---------+
# product_id is a foreign key to the Product table.
# Each row contains a record of a sale, and duplicates are possible.

# Problem Statement:
# Write a function to report products that were sold only in the first quarter of 2019.
# Return the result with 'product_id' and 'product_name' in any order.

# Solution

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # I identify all product_ids that had sales outside the first quarter of 2019
    filter_series = sales.loc[
        (sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31'),
        'product_id'
    ].unique()
    
    # I merge product names into the sales table, filter for sales in the first quarter of 2019,
    # exclude product_ids in filter_series, select relevant columns, and drop duplicates
    return (
        sales
        .merge(product, how='left', on='product_id')[['product_id', 'product_name', 'sale_date']]
        .loc[
            lambda x: 
            (x['sale_date'] >= '2019-01-01') & 
            (x['sale_date'] <= '2019-03-31') & 
            (~x['product_id'].isin(filter_series)),
            ['product_id', 'product_name']
        ]
        .drop_duplicates()
    )

# Intuition:
# - I need to find products sold exclusively in the first quarter of 2019.
# - To do this, I first identify product_ids that had any sale before or after this period.
# - I then merge product names into the sales data to prepare for filtering.
# - I keep only sales within the first quarter of 2019 and exclude any product_ids that appeared outside this window.
# - Finally, I select the unique product_id and product_name pairs.

# Explanation:
# - The first step collects product_ids that appear outside 2019 Q1 to a list (filter_series).
# - The merge brings in product names so I can report them along with IDs.
# - The `.loc[]` filter retains only those sales within 2019 Q1 and removes product_ids that were also sold outside this window.
# - Dropping duplicates ensures that each product appears only once in the final output.
