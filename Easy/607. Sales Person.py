# Problem 607: Sales Person
# Difficulty: Easy

# Table: SalesPerson
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | sales_id        | int     |
# | name            | varchar |
# | salary          | int     |
# | commission_rate | int     |
# | hire_date       | date    |
# +-----------------+---------+
# sales_id is the primary key.
# Each row indicates a salesperson's ID, name, salary, commission rate, and hire date.

# Table: Company
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | com_id      | int     |
# | name        | varchar |
# | city        | varchar |
# +-------------+---------+
# com_id is the primary key.
# Each row indicates a company's ID, name, and city.

# Table: Orders
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | order_id    | int  |
# | order_date  | date |
# | com_id      | int  |
# | sales_id    | int  |
# | amount      | int  |
# +-------------+------+
# order_id is the primary key.
# com_id references Company.com_id.
# sales_id references SalesPerson.sales_id.
# Each row contains order information including the company and salesperson involved.

# Problem Statement:
# I need to find the names of all salespersons who did not have any orders related to the company named "RED".
# I will return the result table in any order.

# Solution

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I start by merging orders with company to get company names on each order
    merged_orders = orders.merge(company, how='left', on='com_id')

    # Next, I merge salespersons with the orders to associate salespersons with companies they sold to
    merged_all = sales_person.merge(merged_orders, how='left', on='sales_id', suffixes=('_sales', '_company'))

    # I identify salespersons who have sold to "RED"
    red_sales_ids = merged_all.loc[merged_all['name_company'] == 'RED', 'sales_id']

    # Finally, I select salespersons who never sold to "RED"
    result = merged_all.loc[~merged_all['sales_id'].isin(red_sales_ids), ['name_sales']]

    # I rename the column, remove duplicates, and reset the index before returning
    return result.rename(columns={'name_sales': 'name'}).drop_duplicates().reset_index(drop=True)

# Intuition:
# - I want to exclude salespersons with orders linked to the company "RED".
# - Joining Orders and Company lets me identify which orders are for "RED".
# - Then, I join SalesPerson with these orders.
# - I filter out salespersons who have any order for "RED".
# - I return the remaining salespersons' names.

# Explanation:
# - `merged_orders` joins orders and companies on `com_id` to get company names.
# - `merged` joins salespersons with orders+companies on `sales_id`.
# - `sales_with_red` is the set of salespersons who have at least one order with "RED".
# - I filter out these salespersons from the full list to get those who never sold to "RED".
# - The result contains unique salesperson names.
