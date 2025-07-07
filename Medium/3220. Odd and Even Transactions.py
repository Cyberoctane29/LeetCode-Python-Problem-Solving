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
# The transaction_id column uniquely identifies each row in this table.

# Problem Statement:
# Write a function to compute the sum of amounts for odd and even transactions for each day.
# If a date has no odd or even transactions, display its sum as 0.
# Return the result table ordered by transaction_date in ascending order.

# Solution

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    # I group the data by transaction_date and compute two aggregations:
    # one for the sum of odd amounts, one for even amounts using lambda filters.
    result_df = transactions.groupby('transaction_date', as_index=False).agg(
        odd_sum=('amount', lambda x: x[x % 2 != 0].sum()),
        even_sum=('amount', lambda x: x[x % 2 == 0].sum())
    )

    # I return the final result
    return result_df

# Intuition:
# I need to calculate the total of odd and even amounts for each unique transaction date.

# Explanation:
# I group the transactions DataFrame by `transaction_date`.
# Then, I use `.agg()` with two lambdas:
# - One lambda filters amounts where value mod 2 is not zero (odd) and sums them.
# - The other filters amounts where value mod 2 is zero (even) and sums them.
# This produces two new columns: `odd_sum` and `even_sum`.
# Finally, I return this aggregated result ordered by date (since groupby preserves order by default if dates are sorted).
