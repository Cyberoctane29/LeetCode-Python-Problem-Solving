# Problem 3220: Odd and Even Transactions
# Difficulty: Medium

# Table: transactions
# +------------------+------+
# | Column Name      | Type |
# +------------------+------+
# | transaction_id   | int  |
# | amount           | int  |
# | transaction_date | date |
# +------------------+------+
# transaction_id is the primary key (column with unique values) for this table.

# Problem Statement:
# Write a function to find the sum of amounts for odd and even transactions for each day.
# If there are no odd or even transactions for a specific date, display as 0.
# Return the result table ordered by transaction_date in ascending order.

# Solution

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    temp_df = transactions.groupby('transaction_date', as_index=False).agg(
        odd_sum=('amount', lambda x: x[x % 2 != 0].sum()),
        even_sum=('amount', lambda x: x[x % 2 == 0].sum())
    )
    return temp_df

# Intuition:
# I want to compute the total of odd and even amounts separately for each date.

# Explanation:
# I group the DataFrame by `transaction_date`.
# Within each group, I calculate two aggregates:
# - `odd_sum`: sum of amounts where the value is odd.
# - `even_sum`: sum of amounts where the value is even.
# I use lambda functions to filter and sum the relevant subsets.
# The result is returned as a DataFrame ordered by date automatically because groupby preserves the order.
