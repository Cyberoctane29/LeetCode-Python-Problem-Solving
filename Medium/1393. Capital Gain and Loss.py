# Problem 1393: Capital Gain/Loss
# Difficulty: Medium

# Table: Stocks
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | stock_name    | varchar |
# | operation     | enum    |
# | operation_day | int     |
# | price         | int     |
# +---------------+---------+
# (stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
# The operation column is an ENUM (category) of type ('Sell', 'Buy').
# Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
# It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day.
# It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.

# Problem Statement:
# Write a function to report the Capital gain/loss for each stock.
# The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
# Return the result table in any order.

# Solution 1

import pandas as pd
import numpy as np

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    # I create a new column 'signed_price' where Buy prices are made negative and Sell prices remain positive
    stocks['signed_price'] = np.where(stocks['operation'] == 'Buy', -stocks['price'], stocks['price'])
    
    # I group by 'stock_name' and sum the signed prices to compute total capital gain or loss
    result_df = stocks.groupby('stock_name', as_index=False).agg(capital_gain_loss=('signed_price', 'sum'))
    
    # I return the final result
    return result_df

# Intuition:
# I need to compute the net profit or loss by treating Buy prices as negative and Sell prices as positive.
# Summing these adjusted prices for each stock will give the total capital gain or loss.

# Explanation:
# I use `np.where` to create a 'signed_price' column where 'Buy' prices are multiplied by -1 and 'Sell' prices remain as is.
# Then, I group the DataFrame by 'stock_name' and sum the 'signed_price' values.
# This sum represents the net capital gain or loss for each stock.
# I finally return this summarized DataFrame.

# Solution 2

import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    # I create a new column 'signed_price' using apply to assign negative price for 'Buy' and positive for 'Sell'
    stocks['signed_price'] = stocks.apply(lambda row: -row['price'] if row['operation'] == 'Buy' else row['price'], axis=1)
    
    # I group by 'stock_name' and sum the signed prices to compute total capital gain or loss
    result_df = stocks.groupby('stock_name', as_index=False).agg(capital_gain_loss=('signed_price', 'sum'))
    
    # I return the final result
    return result_df

# Intuition:
# Similar to Solution 1 — I need to assign a sign to each price based on the operation type.
# Summing these signed prices per stock will yield the total capital gain or loss.

# Explanation:
# I use `apply` with `axis=1` to iterate row-wise and assign a negative price for 'Buy' operations and a positive price for 'Sell'.
# After creating the 'signed_price' column, I group the DataFrame by 'stock_name' and sum the 'signed_price' values.
# This sum represents the net capital gain or loss for each stock.
# The result is returned as a summarized DataFrame.
