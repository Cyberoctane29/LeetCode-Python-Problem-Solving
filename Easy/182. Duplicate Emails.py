# Problem 182: Duplicate Emails
# Difficulty: Easy

# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.

# Problem Statement:
# Write a function to report all duplicate emails.
# The email field is guaranteed to be non-null.
# Return the result table in any order.

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_count = {}  # Dictionary to store email counts

    # Count occurrences of each email
    for email in person['email']:
        email_count[email] = email_count.get(email, 0) + 1

    # Filter emails that appear more than once
    duplicated_emails = [email for email, count in email_count.items() if count > 1]

    # Return as a DataFrame
    return pd.DataFrame({'Email': duplicated_emails})

# Intuition:
# - I need to identify emails that appear more than once in the `email` column.
# - Since `id` is unique but emails can be duplicated, I count occurrences of each email.

# Explanation:
# - I iterate through `person['email']` and count occurrences using a dictionary.
# - I filter out emails that appear more than once.
# - The result is converted into a DataFrame with a column named "Email".
