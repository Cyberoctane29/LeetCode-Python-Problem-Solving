# Problem 1321: Restaurant Growth
# Difficulty: Medium

# Table: Customer
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# | visited_on    | date    |
# | amount        | int     |
# +---------------+---------+
# In SQL, (customer_id, visited_on) is the primary key for this table.
# This table contains data about customer transactions in a restaurant.
# visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
# amount is the total paid by a customer.

# Problem Statement:
# You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).
# Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). 
# average_amount should be rounded to two decimal places.
# Return the result table ordered by visited_on in ascending order.

# Solution

import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    # I first group the customer table by 'visited_on' and sum the 'amount' for each day
    temp_df = customer.groupby('visited_on', as_index=False)['amount'].sum()
    
    # I create a copy of this aggregated DataFrame for further calculations
    result_df = temp_df.copy()
    
    # I define a rolling window of 7 days over the 'amount' column
    roll = temp_df['amount'].rolling(window=7)
    
    # I calculate the total amount and average amount over the 7-day window
    result_df['amount'] = roll.sum()
    result_df['average_amount'] = round(roll.mean(), 2)
    
    # I return the result, filtering out rows where the moving average is not available (i.e., first 6 records)
    return result_df.loc[result_df['average_amount'].notna(),]

# Intuition:
# I need to compute a 7-day moving average of daily total amounts.
# By grouping and summing daily totals, then applying a rolling window, I can track revenue trends.

# Explanation:
# I start by grouping the data by 'visited_on' to get daily total amounts.
# I then use `rolling(window=7)` on the 'amount' column to calculate a moving sum and mean.
# The moving average is rounded to 2 decimal places.
# Finally, I filter out rows where the rolling average is not yet available (less than 7 records) before returning the result.
