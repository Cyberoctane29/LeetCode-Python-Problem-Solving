# Problem 1068: Product Sales Analysis I
# Difficulty: Easy

# Table: Sales
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) is the primary key (combination of columns with unique values) of this table.
# product_id is a foreign key to the Product table.
# Each row of this table shows a sale on the product product_id in a certain year.
# Note that the price is per unit.

# Table: Product
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# +--------------+---------+
# product_id is the primary key of this table.
# Each row indicates the product name for each product.

# Problem Statement:
# Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
# Return the resulting table in any order.

#solution

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # I merge the Sales and Product tables on 'product_id' using a left join to retain all sales records
    merged_df = sales.merge(product, how='left', on='product_id')
    # I select only the required columns: product_name, year, and price for the final result
    return merged_df[['product_name','year','price']]

# Intuition for Solution:
# - I need to combine product details with sales data so that I can access product names for each sale.
# - I merge the Sales and Product tables on the common 'product_id' column to align each sale with its product name.
# - I retain all sales records using a left join and then pick only the relevant columns for the final result.

# Explanation for Solution:
# - I start by merging the Sales and Product tables on 'product_id' with a left join to ensure no sales record is lost.
# - I select only the product_name, year, and price columns since the problem statement requires these three details.
# - I return the resulting DataFrame containing the required information for each sale record.
