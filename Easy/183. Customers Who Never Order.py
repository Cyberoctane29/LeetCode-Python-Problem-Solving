# Problem 183: Customers Who Never Order
# Difficulty: Easy

# Table: Customers
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.

# Table: Orders
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

# Problem Statement:
# Write a function to find all customers who never order anything.
# Return the result table in any order.

# Solution

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers.loc[~customers['id'].isin(orders['customerId']), ['name']].rename(columns={'name': 'Customers'})

# Intuition:
# - I need to find customers who have never placed an order.
# - The `Orders` table contains `customerId`, which links to `id` in `Customers`.
# - I filter out customers whose `id` appears in the `customerId` column of `Orders`.

# Explanation:
# - `customers['id'].isin(orders['customerId'])` checks which customers have placed orders.
# - `~` negates the condition to get customers who haven't placed orders.
# - `.loc[... , ['name']]` selects only the `name` column.
# - `.rename(columns={'name': 'Customers'})` renames the column to match the expected output.
