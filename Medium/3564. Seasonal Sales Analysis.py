# Problem 3564: Seasonal Sales Analysis
# Difficulty: Medium

# Table: sales
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | sale_id       | int     |
# | product_id    | int     |
# | sale_date     | date    |
# | quantity      | int     |
# | price         | decimal |
# +---------------+---------+

# Table: products
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | product_name  | varchar |
# | category      | varchar |
# +---------------+---------+

# Problem Statement:
# Write a function to determine the most popular product category for each season, where:
# - Winter: December, January, February
# - Spring: March, April, May
# - Summer: June, July, August
# - Fall: September, October, November
# Popularity is based on total quantity sold. In case of a tie, prefer the one with higher total revenue (quantity × price).
# Return result ordered by season ascending.

# Solution

import pandas as pd
import numpy as np

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # I convert sale_date to datetime and assign seasons using np.select with boolean masks
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    sales['season'] = np.select(
        [
            sales['sale_date'].dt.month.isin([12, 1, 2]),
            sales['sale_date'].dt.month.isin([3, 4, 5]),
            sales['sale_date'].dt.month.isin([6, 7, 8]),
            sales['sale_date'].dt.month.isin([9, 10, 11])
        ],
        ['Winter', 'Spring', 'Summer', 'Fall'],
        default='Unknown'
    )

    # I compute revenue for each sale
    sales['revenue'] = sales['quantity'] * sales['price']

    # I merge sales with product categories
    merged_df = pd.merge(sales, products, how='left', on='product_id')

    # I compute total quantity and total revenue for each (season, category)
    temp_df1 = merged_df.groupby(['season', 'category'], as_index=False).agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('revenue', 'sum')
    )

    # I pick the top category for each season based on quantity, breaking ties by revenue
    def pick_category(group):
        top_quantity = group['total_quantity'].max()
        candidates = group[group['total_quantity'] == top_quantity]
        if len(candidates) == 1:
            return candidates.iloc[0]
        else:
            return candidates.loc[candidates['total_revenue'].idxmax()]

    result_df = temp_df1.groupby('season').apply(pick_category).reset_index(drop=True)

    # I sort by season in ascending order and return
    return result_df.sort_values(by='season', ascending=True)

# Intuition:
# I first assign seasons based on sale dates using np.select.
# Then I compute total quantity sold and total revenue for each (season, category).
# To identify the most popular category per season, I first pick by highest quantity sold.
# In case of a tie, I break it by selecting the one with the highest total revenue.
# Finally, I return the result sorted by season.

# Explanation:
# The logic relies on grouping sales by season and product category, then summarizing quantities and revenues.
# np.select is ideal for assigning labels based on multiple conditions efficiently.
# I resolve ties by first filtering categories with max quantity, then using idxmax on revenue to pick the winner.
# The final result contains the top category for each season sorted in order.
