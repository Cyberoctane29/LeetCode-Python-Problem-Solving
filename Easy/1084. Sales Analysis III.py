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
# product_id is the primary key for this table.

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
# Each row contains information about one sale.

# Problem Statement:
# Write a function to return products that were only sold in the first quarter of 2019 (2019-01-01 to 2019-03-31 inclusive).
# Products sold before or after this period should be excluded.

# Solution 1

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # I convert 'sale_date' to datetime to enable date filtering
    # I create a list of product_ids with sales outside the target date range
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    filter_series = sales.loc[
        (sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31'),
        'product_id'
    ].unique()
    
    # I merge product and sales data, filter for sales in Q1 2019, and exclude product_ids in filter_series
    # I then select 'product_id' and 'product_name', and remove duplicates
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

# Intuition for Solution 1:
# - I need to identify products that were sold exclusively in the first quarter of 2019.
# - I start by converting the 'sale_date' column to datetime for proper filtering.
# - Then, I extract the list of product_ids with any sale outside the desired date range.
# - I merge the product and sales tables, then filter for sales within the quarter while excluding product_ids from the earlier list.
# - Finally, I select the necessary columns and remove duplicates to get the distinct product list.

# Explanation for Solution 1:
# - Converting 'sale_date' allows me to apply date comparisons.
# - Extracting product_ids with sales outside the range ensures I can later exclude them.
# - The merge brings product names alongside sales data.
# - I filter for Q1 2019 sales and exclude any product in the out-of-range list.
# - Using `.drop_duplicates()` ensures no repeated product records in the final result.


# Solution 2

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # I convert 'sale_date' to datetime for proper filtering
    # I extract product_ids with sales outside the target date range
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    filter_series = sales.loc[
        (sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31'),
        'product_id'
    ].unique()
    
    # I merge product and sales data, use .between() to filter sales within Q1 2019
    # I exclude product_ids present in filter_series
    # Finally, I select relevant columns and remove duplicates
    return (
        sales
        .merge(product, how='left', on='product_id')[['product_id', 'product_name', 'sale_date']]
        .loc[
            lambda x: 
            x['sale_date'].between('2019-01-01', '2019-03-31', inclusive='right') &
            (~x['product_id'].isin(filter_series)),
            ['product_id', 'product_name']
        ]
        .drop_duplicates()
    )

# Intuition for Solution 2:
# - This solution follows a very similar strategy to Solution 1 but uses the `.between()` method for date filtering.
# - I start by converting 'sale_date' for datetime operations.
# - I gather product_ids with any sales outside the target date range.
# - After merging product and sales data, I use `.between()` for a clean and readable date filter.
# - I exclude unwanted product_ids, select required columns, and drop duplicates.

# Explanation for Solution 2:
# - Converting 'sale_date' to datetime allows date filtering.
# - Using `.between()` makes the date condition more readable and concise.
# - Excluding product_ids from filter_series ensures only products sold exclusively in Q1 2019 are kept.
# - Merging helps get product names alongside their sales.
# - The result is deduplicated to retain only distinct products matching the criteria.
