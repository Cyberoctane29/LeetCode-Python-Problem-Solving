# Problem 1484: Group Sold Products By The Date
# Difficulty: Easy

# Table: Activities
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | sell_date   | date    |
# | product     | varchar |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.

# Problem Statement:
# Write a function to find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.
# Return the result table ordered by sell_date.

# Solution

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # I convert the 'sell_date' column to datetime format to ensure correct date operations
    activities['sell_date'] = pd.to_datetime(activities['sell_date'])

    # I group the data by 'sell_date', then calculate:
    # 1. The number of unique products sold on each date using nunique()
    # 2. The concatenated, lexicographically sorted list of unique product names sold on each date
    result_df = activities.groupby(['sell_date'], as_index=False).agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(x.unique())))
    )

    # I return the final result
    return result_df

# Intuition:
# I need to determine for each date how many different products were sold and list their names in sorted order.
# To achieve this, I will group the Activities table by sell_date.
# Then, I will count the number of unique products per date and concatenate the unique product names sorted lexicographically.
# Finally, I will order the result by sell_date.

# Explanation:
# I start by converting the 'sell_date' column to datetime format for consistent handling.
# Then, I group the data by 'sell_date'.
# Inside the aggregation:
# - I use nunique() to count how many distinct products were sold on each date.
# - I use a lambda function to sort the unique product names for each date and join them with commas.
# Lastly, I return the resulting DataFrame as required.
