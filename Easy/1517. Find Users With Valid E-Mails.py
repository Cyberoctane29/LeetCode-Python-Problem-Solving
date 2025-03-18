# Problem 1517: Find Users With Valid E-Mails
# Difficulty: Easy

# Table: Users
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# | mail          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains information of the users signed up on a website. Some e-mails are invalid.

# Problem Statement:
# Write a function to find the users who have valid emails.
# A valid email has:
# - A prefix name that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'.
# - The prefix name must start with a letter.
# - The domain must be '@leetcode.com'.
# Return the result table in any order.

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Use regex to filter the valid email addresses
    return users.loc[users['mail'].str.match(r"^[a-zA-Z][\w.-]*@leetcode\.com$"), ['user_id', 'name', 'mail']]

# Intuition:
# - We need to check if the email matches the required pattern.
# - The email should start with a letter and contain valid characters such as letters, digits, underscores, periods, or dashes.
# - The domain should strictly be '@leetcode.com'.
# - We can use regular expressions (regex) to validate the email format.

# Explanation:
# - `str.match()` is used with a regular expression to check if each email starts with a letter, contains valid characters, and ends with '@leetcode.com'.
# - The regex `^[a-zA-Z][\w.-]*@leetcode\.com$` ensures:
#   - `^[a-zA-Z]`: The email starts with a letter (either upper or lowercase).
#   - `[\w.-]*`: After the first letter, the email can contain letters, digits, underscores, periods, or dashes.
#   - `@leetcode\.com$`: The email must end with '@leetcode.com'.
# - The function returns the `user_id`, `name`, and `mail` of users with valid emails.
