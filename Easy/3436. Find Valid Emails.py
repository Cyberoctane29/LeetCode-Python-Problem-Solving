# Problem 3436: Find Valid Emails
# Difficulty: Easy

# Table: Users
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | user_id         | int     |
# | email           | varchar |
# +-----------------+---------+
# (user_id) is the unique key for this table.
# Each row contains a user's unique ID and email address.

# Problem Statement:
# Write a function to find all valid email addresses from the Users table.
# A valid email address must satisfy the following conditions:
# - It contains exactly one '@' symbol.
# - It ends with '.com'.
# - The part before the '@' contains only alphanumeric characters and underscores.
# - The part after the '@' and before '.com' contains a domain name with only letters.

# Solution

import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # I use str.contains() with a regular expression to filter valid emails
    result_df = users[users['email'].str.contains(r'^[\w]+@[A-Za-z]+\.com$', regex=True)]
    
    # I sort the result by user_id as required
    return result_df.sort_values(by='user_id')

# Intuition:
# I need to select valid emails based on a specific format.
# A regular expression is the most efficient way to validate string patterns like emails.
# I can then use pandas' str.contains() to apply this regex on the 'email' column.

# Explanation:
# I use a regex pattern `^[\w]+@[A-Za-z]+\.com$`:
# - `^[\w]+` ensures the string starts with one or more alphanumeric characters or underscores.
# - `@` matches the '@' symbol exactly once.
# - `[A-Za-z]+` matches one or more uppercase or lowercase letters (for the domain name).
# - `\.com$` ensures the string ends with '.com'.
# I filter the DataFrame using this pattern via str.contains().
# I sort the resulting DataFrame by 'user_id' to get the final output in the required order.
# Lastly, I return the sorted DataFrame.
