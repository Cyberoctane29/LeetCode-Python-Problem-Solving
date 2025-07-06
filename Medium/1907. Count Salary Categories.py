# Problem 1907: Count Salary Categories
# Difficulty: Medium

# Table: Accounts
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | income      | int  |
# +-------------+------+
# account_id is the primary key (column with unique values) for this table.
# Each row contains information about the monthly income for one bank account.

# Problem Statement:
# Write a function to calculate the number of bank accounts for each salary category.
# The salary categories are:
# - "Low Salary": salaries strictly less than $20000.
# - "Average Salary": salaries between $20000 and $50000 inclusive.
# - "High Salary": salaries strictly greater than $50000.
# The result table must contain all three categories, with a count of 0 if no accounts fall into a category.
# Return the result table in any order.

# Solution 1

import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # I assign a 'category' to each row based on income ranges using np.select
    accounts['category'] = np.select(
        [(accounts['income'] < 20000),
         ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)),
         (accounts['income'] > 50000)],
        ['Low Salary', 'Average Salary', 'High Salary']
    )

    # I count the number of occurrences of each category, reindex missing categories to zero
    result_df = accounts['category'].value_counts().reindex(
        ['Low Salary', 'Average Salary', 'High Salary'],
        fill_value=0
    ).reset_index().rename(columns={'count': 'accounts_count'})

    # I return the result
    return result_df

# Intuition:
# I need to categorize each account based on its income and count how many accounts fall into each category.

# Explanation:
# I use `np.select` to classify each row into one of three salary categories.
# Then, I use `value_counts()` to count the number of accounts in each category.
# I reindex the result to ensure all three categories appear, filling any missing counts with 0.
# Finally, I format the result by resetting the index and renaming the count column.

# Solution 2

import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # I assign a 'category' to each row based on income ranges using np.select
    accounts['category'] = np.select(
        [(accounts['income'] < 20000),
         ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)),
         (accounts['income'] > 50000)],
        ['Low Salary', 'Average Salary', 'High Salary']
    )

    # I group by category and count number of accounts, then reindex to include missing categories
    result_df = accounts.groupby('category').agg(accounts_count=('account_id', 'count'))
    result_df = result_df.reindex(['Low Salary', 'Average Salary', 'High Salary'], fill_value=0).reset_index()

    # I return the result
    return result_df

# Intuition:
# Similar to Solution 1, but using groupby instead of value_counts to compute the category counts.

# Explanation:
# I classify incomes into categories using `np.select`.
# Then, I group the DataFrame by the 'category' column and count the number of accounts in each group.
# I reindex to ensure all categories are included in the result, even those with zero accounts.
# Finally, I reset the index to return a clean DataFrame.

# Solution 3

import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # I assign a 'category' to each row based on income ranges using np.select
    accounts['category'] = np.select(
        [(accounts['income'] < 20000),
         ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)),
         (accounts['income'] > 50000)],
        ['Low Salary', 'Average Salary', 'High Salary']
    )
    # I explicitly declare 'category' as a Categorical type with ordered categories
    accounts['category'] = pd.Categorical(
        accounts['category'],
        categories=['Low Salary', 'Average Salary', 'High Salary']
    )

    # I group by category and count number of accounts with categorical order enforced
    result_df = accounts.groupby('category', as_index=False, observed=False).agg(accounts_count=('account_id', 'count'))

    # I return the result
    return result_df

# Intuition:
# I need to assign categories, then count accounts while preserving a specific order for categories.

# Explanation:
# I use `np.select` to assign categories based on income.
# I convert the 'category' column to a `pd.Categorical` type with an explicit category order.
# I group by this categorical column and count the number of accounts in each group.
# Because the categorical type is defined, the resulting DataFrame automatically respects the desired order without needing reindexing.
# I finally return this summarized DataFrame.
