# Problem 586: Customer Placing the Largest Number of Orders
# Difficulty: Easy

# Table: Orders
# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# order_number is the primary key (column with unique values) for this table.
# This table contains information about the order ID and the customer ID.

# Problem Statement:
# Write a function to find the customer_number for the customer who has placed the largest number of orders.
# The test cases guarantee exactly one customer has placed more orders than any other.

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame({'customer_number': []})
    # I count the occurrences of each customer_number, then find the one with the highest count.
    return pd.DataFrame({'customer_number': [orders['customer_number'].value_counts().idxmax()]})

# Intuition:
# - I need to find the customer who has placed the most orders.
# - Counting orders per customer and selecting the max count will give me the desired customer.

# Explanation:
# - I use `value_counts()` on 'customer_number' to get the frequency of orders per customer.
# - I use `idxmax()` to find the customer with the highest order count.
# - If the orders DataFrame is empty, I return an empty DataFrame.
# - Otherwise, I return the customer_number in a DataFrame as specified.
