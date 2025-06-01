# Problem 584: Find Customer Referee
# Difficulty: Easy

# Table: Customer
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

# Problem Statement:
# Write a function to find the names of customers not referred by the customer with id = 2.
# Return the result table in any order.

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.loc[(customer['referee_id'] != 2) | (customer['referee_id'].isnull()), ['name']]

# Intuition:
# - I need to identify customers whose `referee_id` is not 2.
# - Additionally, some customers may not have a referee at all (null), so I also include those.

# Explanation:
# - I use `.loc[]` to filter the rows where `referee_id` is not 2 or is null.
# - I then select only the `name` column for the final result.
# - The result is returned as a DataFrame.