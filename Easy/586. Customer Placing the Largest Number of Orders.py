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
# Write a function to find the `customer_number` for the customer who has placed the largest number of orders.
# It is guaranteed that exactly one customer has placed more orders than any other.

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])
    return pd.DataFrame({'customer_number': [orders['customer_number'].value_counts().idxmax()]})

# Intuition:
# - I need to count how many times each `customer_number` appears in the `orders` table.
# - The customer with the highest count is the one with the most orders.

# Explanation:
# - I use `value_counts()` to count the occurrences of each `customer_number`.
# - I retrieve the customer with the highest order count using `idxmax()`.
# - I return the result in a DataFrame with the column `customer_number`.
# - I also handle the edge case where the `orders` table might be empty, returning an empty DataFrame with the appropriate column.
