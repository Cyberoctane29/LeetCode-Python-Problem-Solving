# Problem 1211: Queries Quality and Percentage
# Difficulty: Easy

# Table: Queries
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | query_name  | varchar |
# | result      | varchar |
# | position    | int     |
# | rating      | int     |
# +-------------+---------+
# The table may have duplicate rows.
# 'position' ranges from 1 to 500.
# 'rating' ranges from 1 to 5, and a rating less than 3 is considered a poor query.

# Problem Statement:
# I need to compute, for each query_name:
# - the average query quality (defined as the mean of rating/position)
# - and the percentage of queries with a rating less than 3 (poor queries).
# Both should be rounded to 2 decimal places.

# Solution

import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # I group the DataFrame by 'query_name' since stats need to be calculated per query
    result_df = queries.groupby('query_name').apply(
        lambda x: pd.Series({
            # I calculate query quality as the mean of (rating / position) for each query_name and round to 2 decimals
            'quality': ((x['rating'] / x['position']).mean() + 1e-10).round(2),
            # I calculate the poor query percentage as the mean of (rating < 3), multiply by 100 for percentage, and round
            'poor_query_percentage': (((x['rating'] < 3).mean() * 100) + 1e-10).round(2)
        })
    ).reset_index()
    # Finally, I reset the index so query_name becomes a regular column again
    return result_df

# Intuition:
# I need to compute two aggregated values for each query_name: 
# - the average of (rating / position)
# - and the percentage of records with a rating less than 3.
# Grouping by query_name allows me to calculate these metrics individually for each group.

# Explanation:
# I first group the DataFrame by 'query_name' so I can compute statistics for each query.
# Inside apply, I use pd.Series to construct a Series with two values:
# - 'quality' is calculated as the mean of (rating / position) for that query_name group.
# - 'poor_query_percentage' is the mean of boolean values (rating < 3), multiplied by 100 to convert it to a percentage.
# I add a small value (1e-10) before rounding to safely handle any floating-point rounding edge cases.
# Finally, I reset the index to turn 'query_name' back into a regular column in the result.
