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
    # I group the customer table by 'visited_on' and sum the 'amount' for each day
    temp_df = customer.groupby('visited_on', as_index=False)['amount'].sum()
    
    # I create a copy of this aggregated DataFrame for further calculations
    result_df = temp_df
    
    # I define a rolling window of 7 days over the 'amount' column
    roll = temp_df['amount'].rolling(window=7)
    
    # I compute the rolling sum and assign it to the 'amount' column
    result_df['amount'] = roll.sum()
    
    # I compute the rolling mean, round it to 2 decimal places, and assign it to 'average_amount'
    result_df['average_amount'] = round(roll.mean(), 2)
    
    # I return the final result excluding rows with NaN average values (i.e., the first 6 days)
    return result_df.loc[result_df['average_amount'].notna(), ]

# Intuition:
# I need to calculate the total and average amount paid by customers in a moving window of 7 consecutive days.
# Using `rolling` on the summed daily amounts allows me to efficiently compute these metrics.

# Explanation:
# I first aggregate the daily total amounts by grouping the data on 'visited_on' and summing 'amount'.
# I then create a rolling window of 7 days over the 'amount' column.
# Using `sum()` and `mean()`, I calculate the total and average amounts for each 7-day window.
# I round the averages to two decimal places.
# Finally, I filter out the rows where the rolling average is NaN (which occurs for the initial 6 days before a full window is available).
