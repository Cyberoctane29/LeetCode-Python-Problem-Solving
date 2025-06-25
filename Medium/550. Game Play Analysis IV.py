# Problem 550: Game Play Analysis IV
# Difficulty: Medium

# Table: Activity
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

# Problem Statement:
# Write a function to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places.
# In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

# Solution

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # I count the total number of unique players
    player_count = len(activity['player_id'].unique())
    
    # I group the data by player_id to find each player's first login date
    # and check if they logged in on the next day
    result_df = activity.groupby('player_id', as_index=False).agg(
        first_login=('event_date', 'min'),
        if_next_day=('event_date', lambda x: (x.min() + pd.Timedelta(days=1)) in x.values)
    )
    
    # I compute the fraction of players who logged in again the next day, rounded to 2 decimal places
    return pd.DataFrame({'fraction': [round((result_df['if_next_day'].sum() / player_count), 2)]})

# Intuition:
# I need to identify each player's first login date, then check whether they logged in again the following day.
# Finally, I calculate the fraction of such players out of the total number of unique players.

# Explanation:
# I start by counting the total number of unique players using `unique()` on the 'player_id' column.
# Then, I use `groupby` on 'player_id' to compute two values:
# - The first login date using `min()`.
# - Whether the player logged in on the day after their first login using a lambda function with `pd.Timedelta(days=1)` and membership check in x.values.
# After the groupby operation, I calculate the sum of players who logged in the next day, divide it by the total number of players, and round the result to two decimal places.
# I return the final result in a DataFrame with a single column named 'fraction'.
