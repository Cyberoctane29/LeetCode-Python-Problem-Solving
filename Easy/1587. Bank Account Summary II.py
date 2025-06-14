# Problem 1587: Bank Account Summary II
# Difficulty: Easy

# Table: Users
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | account      | int     |
# | name         | varchar |
# +--------------+---------+
# account is the primary key (column with unique values) for this table.
# Each row of this table contains the account number of each user in the bank.
# There will be no two users having the same name in the table.

# Table: Transactions
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | trans_id      | int     |
# | account       | int     |
# | amount        | int     |
# | transacted_on | date    |
# +---------------+---------+
# trans_id is the primary key (column with unique values) for this table.
# Each row of this table contains all changes made to all accounts.
# amount is positive if the user received money and negative if they transferred money.
# All accounts start with a balance of 0.

# Problem Statement:
# Write a function to report the name and balance of users with a balance higher than 10000.
# The balance of an account is equal to the sum of the amounts of all transactions involving that account.
# Return the result table in any order.

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # I group the Transactions table by account and sum the amount to get the final balance for each account
    temp_df = transactions.groupby('account', as_index=False).agg(balance=('amount', 'sum'))
    
    # I merge the calculated balances with the Users table using an inner join on account
    merged_df = pd.merge(temp_df, users, how='inner', on='account')
    
    # I filter the merged DataFrame to retain only those users whose balance is greater than 10000
    result_df = merged_df[merged_df['balance'] > 10000]
    
    # I select the name and balance columns for the final result
    return result_df[['name', 'balance']]

# Intuition:
# I need to find the total balance for each account by summing all transactions.
# Then, I will join this information with the Users table to get the names.
# Finally, I will filter for those users whose balance exceeds 10000 and return their name and balance.

# Explanation:
# I start by grouping the Transactions table by account and calculating the total amount (balance) per account.
# Then, I merge this grouped data with the Users table using an inner join on account to get the corresponding names.
# Next, I filter the merged result to retain only the records where the balance exceeds 10000.
# Lastly, I select only the name and balance columns and return the final result.
