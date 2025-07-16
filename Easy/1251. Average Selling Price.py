# Problem 1251: Average Selling Price  
# Difficulty: Easy

# Table: Prices  
# +---------------+---------+  
# | Column Name   | Type    |  
# +---------------+---------+  
# | product_id    | int     |  
# | start_date    | date    |  
# | end_date      | date    |  
# | price         | int     |  
# +---------------+---------+  
# (product_id, start_date, end_date) is the primary key.

# Table: UnitsSold  
# +---------------+---------+  
# | Column Name   | Type    |  
# +---------------+---------+  
# | product_id    | int     |  
# | purchase_date | date    |  
# | units         | int     |  
# +---------------+---------+

# Problem Statement:  
# Write a function to compute the average selling price for each product.
# The price is valid only between its start_date and end_date.
# Match each unit sold with the correct price based on purchase date.
# The average price is total revenue divided by total units.
# Round the final average_price to 2 decimal places.
# If a product has no units sold, its average_price should be 0.

# Solution 1

import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(prices, units_sold, how='left', on='product_id')
    merged_df = merged_df[(merged_df['purchase_date'].isna()) | ((merged_df['purchase_date'] >= merged_df['start_date']) & (merged_df['purchase_date'] <= merged_df['end_date']))]

    merged_df = merged_df['units'].fillna(0)

    result_df = merged_df.groupby(by='product_id').apply(
        lambda x: pd.Series({
            'average_price': round((x['price'] * x['units']).sum() / x['units'].sum(), 2) if x['units'].sum() != 0 else 0
        })
    )
    return result_df

# Intuition:
# I join prices and units_sold on product_id, keeping only purchases within valid pricing windows.
# Then, I compute total revenue as price × units for each valid row.
# Finally, I divide total revenue by total units to compute the average price.
# If no units were sold, the average price is returned as 0.

# Explanation:
# The key logic is date filtering to ensure each purchase is matched with the right price.
# Missing sales are handled using fillna(0).
# I group by product_id and compute average price only where units > 0.

# Solution 2

import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(prices, units_sold, how='left', on='product_id')

    merged_df = merged_df[
        (merged_df['purchase_date'] >= merged_df['start_date']) &
        (merged_df['purchase_date'] <= merged_df['end_date'])
    ]

    merged_df['revenue'] = merged_df['price'] * merged_df['units']

    agg_df = merged_df.groupby('product_id', as_index=False).agg(
        total_revenue=('revenue', 'sum'),
        total_units=('units', 'sum')
    )

    result = prices[['product_id']].drop_duplicates().merge(agg_df, on='product_id', how='left')
    result['average_price'] = (result['total_revenue'] / result['total_units']).fillna(0).round(2)

    return result[['product_id', 'average_price']]

# Intuition:
# I calculate revenue at row level as price × units.
# Then, I aggregate total revenue and total units per product.
# I join this with all unique products from the Prices table to ensure all products are included.
# Finally, I compute average price as revenue / units, rounding and handling NaNs with fillna(0).

# Explanation:
# The approach cleanly separates matching, aggregation, and final computation.
# By using total sums explicitly and ensuring outer join with all products, I guarantee correct handling of products with zero sales.
