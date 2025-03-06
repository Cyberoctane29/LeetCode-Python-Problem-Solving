# Problem 2882: Drop Duplicate Rows
# Difficulty: Easy

# Problem Statement:
# Write a function to remove duplicate rows from the `customers` DataFrame based on the `email` column.
# Keep only the first occurrence of each unique email.

# Solution

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=['email'], keep='first')
    return customers

# Intuition:
# - I need to remove duplicate rows where the `email` column has repeating values.
# - The first occurrence of each unique email should be kept.

# Explanation:
# - `drop_duplicates(subset=['email'], keep='first')` removes duplicate rows based on the `email` column.
# - The `keep='first'` parameter ensures that only the first occurrence is retained.
# - The modified DataFrame is returned.