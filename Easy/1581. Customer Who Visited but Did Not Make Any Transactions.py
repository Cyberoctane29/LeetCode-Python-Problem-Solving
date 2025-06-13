# Problem 1581: Customer Who Visited but Did Not Make Any Transactions
# Difficulty: Easy

# Table: Visits
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | visit_id    | int     |
# | customer_id | int     |
# +-------------+---------+
# visit_id is the column with unique values for this table.
# This table contains information about the customers who visited the mall.

# Table: Transactions
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | transaction_id | int     |
# | visit_id       | int     |
# | amount         | int     |
# +----------------+---------+
# transaction_id is the column with unique values for this table.
# This table contains information about the transactions made during the visit_id.

# Problem Statement:
# Write a function to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
# Return the result table sorted in any order.

# Solution

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # I merge the Visits and Transactions tables using a left join on 'visit_id'
    merged_df = pd.merge(visits, transactions, how='left', on='visit_id')

    # I filter the merged DataFrame to retain only those records where 'transaction_id' is null (no transaction made)
    filtered_df = merged_df[merged_df['transaction_id'].isna()][['customer_id', 'transaction_id']]

    # I group the filtered data by 'customer_id' and count the number of visits without transactions for each customer
    result_df = filtered_df.groupby('customer_id', as_index=False).agg(count_no_trans=('customer_id', 'count'))

    # I return the final result
    return result_df

# Intuition:
# I need to find which customers visited the mall but didn’t make any transactions and how many such visits each of them made.
# To do this, I will merge the Visits and Transactions tables on 'visit_id' using a left join.
# Then, I will filter out the rows where 'transaction_id' is null, indicating no transaction was made.
# Finally, I will group these records by 'customer_id' and count the number of visits for each customer.

# Explanation:
# I start by merging the Visits and Transactions tables on 'visit_id' using a left join to keep all visit records.
# Next, I filter the merged table to get only those visits where 'transaction_id' is null, meaning no transaction occurred.
# Then, I group the resulting records by 'customer_id' and use count aggregation to count the number of such visits for each customer.
# Lastly, I return the result containing 'customer_id' and the corresponding count of visits without transactions.
