# Problem 2889: Reshape Data: Pivot
# Difficulty: Easy

# DataFrame `weather`:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | city        | object |
# | month       | object |
# | temperature | int    |
# +-------------+--------+

# Problem Statement:
# Write a function to pivot the `weather` DataFrame so that each row represents 
# temperatures for a specific month, and each city is a separate column.

# Solution

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    answer = weather.pivot(index='month', columns='city', values='temperature')
    return answer

# Intuition:
# - The data needs to be reshaped so that months remain as rows, cities become columns, 
#   and temperature values are placed accordingly.
# - I use the `pivot()` function to transform the DataFrame structure.

# Explanation:
# - `weather.pivot(index='month', columns='city', values='temperature')` reorganizes 
#   the DataFrame by making `month` the index, `city` the columns, and `temperature` the values.
# - The function returns a new DataFrame where each row corresponds to a month, 
#   and each column represents a city's temperatures.
