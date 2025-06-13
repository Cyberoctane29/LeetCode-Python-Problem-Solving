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

# Solution 1

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # I merge the Visits and Transactions tables on visit_id with a left join to retain all visits
    merged_df = pd.merge(visits, transactions, how='left', on='visit_id')
    
    # I filter the merged result for records where transaction_id is null (no transaction made)
    filtered_df = merged_df[merged_df['transaction_id'].isna()][['customer_id', 'transaction_id']]
    
    # I group by customer_id and count the number of such no-transaction visits
    result_df = filtered_df.groupby('customer_id', as_index=False).agg(count_no_trans=('customer_id', 'count'))
    
    # I return the final result
    return result_df

# Intuition:
# I need to find customers who visited but didn’t make a transaction.
# To do this, I will merge the Visits and Transactions tables on visit_id using a left join.
# Then, I will filter for rows where transaction_id is null.
# Finally, I will group these by customer_id and count the number of such visits.

# Explanation:
# I start by merging the Visits and Transactions tables on visit_id, retaining all records from Visits.
# Then, I filter the resulting DataFrame for rows where transaction_id is null — indicating no transaction.
# I select the customer_id and transaction_id columns.
# Next, I group the filtered DataFrame by customer_id and count the number of records for each.
# Finally, I return this grouped DataFrame with customer_id and count_no_trans.

# Solution 2

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # I merge the Visits and Transactions tables on visit_id with a left join to retain all visits
    merged_df = pd.merge(visits, transactions, how='left', on='visit_id')
    
    # I filter the merged result for records where transaction_id is null and get the customer_id series
    filtered_series = merged_df[merged_df['transaction_id'].isna()]['customer_id']
    
    # I count the number of occurrences of each customer_id and reset the index
    result_df = filtered_series.value_counts().reset_index()
    
    # I rename the columns as required
    result_df.columns = ['customer_id', 'count_no_trans']
    
    # I return the final result
    return result_df

# Intuition:
# The task is to find how many times each customer visited without making a transaction.
# I will merge Visits and Transactions tables using a left join.
# Then, I will filter records with null transaction_id and count the number of visits per customer.

# Explanation:
# I merge the two tables on visit_id using a left join to retain all visits.
# Then, I filter for rows where transaction_id is null.
# I extract the customer_id series from these rows.
# I use value_counts() to count how many times each customer_id appears.
# I reset the index to convert it into a DataFrame.
# I rename the columns to customer_id and count_no_trans.
# Finally, I return the resulting DataFrame.
