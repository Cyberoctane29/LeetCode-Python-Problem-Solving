# Problem 1164: Product Price at a Given Date
# Difficulty: Medium

# Table: Products
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | new_price     | int     |
# | change_date   | date    |
# +---------------+---------+
# (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
# Each row of this table indicates that the price of some product was changed to a new price at some date.
# Initially, all products have price 10.

# Problem Statement:
# Write a function to find the prices of all products on the date 2019-08-16.
# Return the result table in any order.

# Solution

import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # I group the Products table by 'product_id'
    # For each product, I check if there’s any price change on or before '2019-08-16'
    # If so, I get the latest applicable price by sorting by 'change_date' in descending order and picking the first
    # If not, I assign the default price of 10
    result_df = products.groupby('product_id', as_index=False).apply(
        lambda x: pd.Series({
            'price': x.loc[x['change_date'] <= pd.to_datetime('2019-08-16'), ]
                            .sort_values(by='change_date', ascending=False)['new_price'].iloc[0]
            if (x['change_date'] <= pd.to_datetime('2019-08-16')).any() else 10
        })
    )
    
    # I return the final result
    return result_df

# Intuition:
# I need to check for each product whether any price changes occurred on or before '2019-08-16'.
# If yes, I pick the most recent price before that date.
# If no, the price remains at the initial value of 10.

# Explanation:
# I use `groupby` on 'product_id' to handle each product separately.
# Within each group, I filter for price changes on or before '2019-08-16'.
# If any exist, I sort these changes by date descendingly and pick the top value using `iloc[0]`.
# If none exist, I assign 10.
# I return the compiled result as a DataFrame listing the product IDs and their prices on '2019-08-16'.
