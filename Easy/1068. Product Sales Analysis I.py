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
    return sales.merge(product, how='left', on='product_id')[['product_name','year','price']]

# Intuition for Solution:
# - I need to associate each sale record with its product name.
# - I merge the two tables on the 'product_id' column using a left join to keep all sales records.
# - I select only the product_name, year, and price columns for the final result as required.

# Explanation for Solution:
# - I perform a left join merge on 'product_id' so that each sale record from the Sales table gets matched with the corresponding product name from the Product table.
# - I filter the merged DataFrame to retain only the product_name, year, and price columns.
# - I return this final DataFrame containing the desired details for each sale.
