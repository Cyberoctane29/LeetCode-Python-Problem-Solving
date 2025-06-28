# Problem 1070: Product Sales Analysis III
# Difficulty: Medium

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
# product_id is a foreign key (reference column) to the Product table.
# Each row records a sale of a product in a given year.
# A product may have multiple sales entries in the same year.
# Note that the per-unit price.

# Problem Statement:
# Write a function to find all sales that occurred in the first year each product was sold.
# For each product_id, identify the earliest year it appears in the Sales table.
# Return all sales entries for that product in that year.
# Return a table with the following columns: product_id, first_year, quantity, and price.

# Solution

import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    # I find the earliest year each product was sold using groupby and min
    temp_df = sales.groupby('product_id', as_index=False).agg(min_year=('year', 'min'))
    
    # I merge the original sales table with this result to get each product's first year alongside its sales data
    merged_df = pd.merge(sales, temp_df, how='left', on='product_id')
    
    # I filter the merged DataFrame to include only records where the sale year matches the product's first year
    result_df = merged_df.loc[merged_df['year'] == merged_df['min_year'], ]
    
    # I rename the 'year' column to 'first_year' and drop unnecessary columns
    return result_df.rename(columns={'year': 'first_year'}).drop(columns=['sale_id', 'min_year'])

# Intuition:
# I need to find the first year each product was sold and then select all sale records from that year.
# Merging the first-year information back with the full sales data allows easy filtering of relevant records.

# Explanation:
# I start by grouping the Sales table by 'product_id' and use `min()` to find the earliest year each product was sold.
# I merge this result with the original Sales table to add a 'min_year' column for each product's sales records.
# I filter the merged DataFrame to keep only those rows where the sale year equals the product's first sale year.
# Finally, I rename the 'year' column to 'first_year' and remove the 'sale_id' and 'min_year' columns before returning the result.
