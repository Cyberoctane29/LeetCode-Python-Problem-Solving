# Problem 1174: Immediate Food Delivery II
# Difficulty: Medium

# Table: Delivery
# +-----------------------------+---------+
# | Column Name                 | Type    |
# +-----------------------------+---------+
# | delivery_id                 | int     |
# | customer_id                 | int     |
# | order_date                  | date    |
# | customer_pref_delivery_date | date    |
# +-----------------------------+---------+
# delivery_id is the column of unique values of this table.
# The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).

# If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
# The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

# Problem Statement:
# Write a function to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

# Solution

import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # I identify the first order for each customer by selecting the row with the minimum order_date per customer
    first_order = delivery.loc[(delivery.groupby('customer_id')['order_date'].idxmin()), ]
    
    # I calculate the percentage of immediate orders where order_date equals customer_pref_delivery_date
    result_df = round((((first_order['order_date'] == first_order['customer_pref_delivery_date']).sum()) / len(first_order)) * 100, 2)
    
    # I return the final result in the required format
    return pd.DataFrame({'immediate_percentage': [result_df]})

# Intuition:
# I need to focus only on each customer's first order, then check how many of these were immediate deliveries.
# Dividing the number of immediate first orders by the total number of customers and multiplying by 100 gives the required percentage.

# Explanation:
# I start by using `groupby` and `idxmin()` to find the index of the earliest order_date for each customer.
# I extract these records as the 'first_order' DataFrame.
# I compare 'order_date' with 'customer_pref_delivery_date' to identify immediate orders and use `.sum()` to count them.
# I compute the percentage, round it to two decimal places, and wrap the result in a DataFrame before returning.
