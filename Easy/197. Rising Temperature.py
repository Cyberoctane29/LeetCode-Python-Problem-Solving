# Problem 197: Rising Temperature
# Difficulty: Easy

# Table: Weather
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is unique for each row.
# No duplicate recordDate values.
# Each row records temperature on that date.

# Problem Statement:
# Find all ids where the temperature is higher than the previous day's temperature.
# Only consider consecutive dates (difference of exactly 1 day).

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # I sort the DataFrame by date to ensure chronological order
    weather.sort_values(by='recordDate', inplace=True)
    
    # I check two conditions:
    # 1. The difference between consecutive dates is exactly one day
    # 2. The temperature difference is positive (temperature rose)
    result = weather.loc[
        (weather['recordDate'].diff().dt.days == 1) & 
        (weather['temperature'].diff() > 0),
        ['id']
    ]
    return result

# Intuition:
# - I need to compare each day's temperature with the previous day's temperature.
# - I only consider dates that are consecutive (difference of exactly 1 day).
# - If the temperature increased on the consecutive day, I select that day's id.

# Explanation:
# - Sorting by 'recordDate' arranges data chronologically.
# - `.diff()` on 'recordDate' gives the day difference between rows.
# - `.diff()` on 'temperature' gives the temperature change between rows.
# - I filter rows where date difference is 1 and temperature difference is positive.
