# Problem 1667: Fix Names in a Table
# Difficulty: Easy

# Table: Users
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. 
# The name consists of only lowercase and uppercase characters.

# Problem Statement:
# Write a function to fix the names so that:
# - Only the first character is uppercase.
# - The rest of the name is lowercase.
# Return the result table ordered by `user_id`.

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id')

# Intuition:
# - Each `name` should have only the first character in uppercase and the rest in lowercase.
# - We can achieve this using the `.str.capitalize()` method in Pandas.
# - This method automatically converts the first character to uppercase and the rest to lowercase.

# Explanation:
# - The `str.capitalize()` method transforms each name in the `name` column.
# - Sorting by `user_id` ensures the result table is in the expected order.
# - This approach is efficient because it applies string operations directly on the DataFrame.
