# Problem 196: Delete Duplicate Emails
# Difficulty: Easy

# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row contains an email with no uppercase letters.

# Problem Statement:
# Delete all duplicate emails, keeping only the record with the smallest id for each unique email.
# For Pandas, modify the `person` DataFrame in place.
# The final Person table is shown after running the code.

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # I sort the DataFrame by 'id' to ensure the smallest id for each email comes first
    person.sort_values(by='id', inplace=True)
    
    # I drop duplicates based on 'email', keeping the first occurrence (smallest id)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)

# Intuition:
# - I want to keep only one unique email, which should have the smallest id.
# - Sorting by 'id' ensures the first occurrence of each email has the smallest id.

# Explanation:
# - Sorting the DataFrame by 'id' places the smallest id first for each email.
# - `drop_duplicates` with `keep='first'` drops subsequent duplicate emails.
# - The operation modifies the DataFrame in place, as required.
