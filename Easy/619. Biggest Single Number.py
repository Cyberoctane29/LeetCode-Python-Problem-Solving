# Problem 19: Biggest Single Number
# Difficulty: Easy

# Table: MyNumbers
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | num         | int  |
# +-------------+------+
# This table may contain duplicates.
# Each row contains an integer.

# Problem Statement:
# Find the largest single number in the table.
# A single number is one that appears exactly once.
# If no single number exists, return null.

# Solution

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # count occurrences of each number
    temp_df = my_numbers['num'].value_counts().reset_index()
    temp_df.columns = ['num', 'count']  # rename columns for clarity
    
    # filter for numbers that appear exactly once (single numbers)
    filtered_df = temp_df.loc[temp_df['count'] == 1, ['num', 'count']]
    
    # if no single numbers exist, return DataFrame with null
    if filtered_df.empty:
        return pd.DataFrame([{'num': None}])
    
    # return the largest single number as a DataFrame
    return pd.DataFrame([{'num': filtered_df['num'].max()}])

# Intuition:
# - I need to find numbers that appear exactly once in the dataset.
# - After identifying those single numbers, I must find the largest among them.
# - If none exist, I return null.

# Explanation:
# - I use `value_counts()` to count occurrences of each number.
# - I filter the counts to keep only those with a count of 1.
# - If the filtered result is empty, I return null.
# - Otherwise, I return the maximum number from those single occurrences.
