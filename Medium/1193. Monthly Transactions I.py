# Problem 1193: Monthly Transactions I
# Difficulty: Medium

# Table: Transactions
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | country       | varchar |
# | state         | enum    |
# | amount        | int     |
# | trans_date    | date    |
# +---------------+---------+
# id is the primary key of this table.
# The table has information about incoming transactions.
# The state column is an enum of type ["approved", "declined"].

# Problem Statement:
# Write a function to find for each month and country:
# - The number of transactions and their total amount
# - The number of approved transactions and their total amount
# Return the result table in any order.

# Solution

import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # I extract the 'month' from 'trans_date' in the format 'YYYY-MM'
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    
    # I group the transactions by 'month' and 'country'
    # For each group, I compute:
    # - total transaction count
    # - approved transaction count
    # - total transaction amount
    # - approved transaction amount
    result_df = transactions.groupby(['month', 'country'], dropna=False, as_index=False).apply(
        lambda x: pd.Series({
            'trans_count': x['id'].count(),
            'approved_count': x.loc[(x['state'] == 'approved'), 'id'].count(),
            'trans_total_amount': x['amount'].sum(),
            'approved_total_amount': x.loc[(x['state'] == 'approved'), 'amount'].sum()
        })
    )
    
    # I return the final aggregated result
    return result_df

# Intuition:
# I need to summarize transaction data month-wise and country-wise.
# This requires both total and approved-specific metrics for each group.

# Explanation:
# I start by creating a new 'month' column from 'trans_date' formatted as 'YYYY-MM'.
# I use `groupby` on 'month' and 'country' and apply a custom aggregation function via `apply`.
# Within each group, I:
# - Count total transactions using `count()`
# - Count approved transactions by filtering where 'state' is 'approved' and counting 'id'
# - Sum total transaction amounts using `sum()`
# - Sum approved transaction amounts similarly after filtering.
# Finally, I return the resulting DataFrame.
