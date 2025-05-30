# Problem 511: Game Play Analysis I
# Difficulty: Easy

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
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some date using some device.

# Problem Statement:
# Write a function to find the first login date for each player.
# Return the result table in any order.

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Sort the activity by event_date so earliest logins appear first
    activity.sort_values(by='event_date', inplace=True)
    
    # Drop duplicate player_id entries, keeping the first occurrence (earliest date)
    activity.drop_duplicates(subset='player_id', keep='first', inplace=True)
    
    # Return the required columns with appropriate renaming
    return activity[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})

# Intuition:
# - I need to identify the earliest login date for each player.
# - Since each player's first login would be the earliest `event_date` associated with their `player_id`, 
#   sorting the DataFrame by `event_date` ensures that the first occurrence per player is their first login.

# Explanation:
# - I sort the DataFrame by `event_date` in ascending order.
# - Then, I use `drop_duplicates()` on the `player_id` column, keeping the first occurrence for each player.
# - Lastly, I select `player_id` and `event_date`, renaming `event_date` to `first_login` for clarity in the output.
