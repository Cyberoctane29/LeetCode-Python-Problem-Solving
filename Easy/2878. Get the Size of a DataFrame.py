# Problem 2878: Get the Size of a DataFrame
# Difficulty: Easy

# DataFrame `players`:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+

# Problem Statement:
# Write a function to calculate and return the number of rows and columns of the given DataFrame `players`.
# The result should be returned as a list in the format: [number of rows, number of columns].

# Solution

import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

# Intuition:
# - I need to determine the number of rows and columns in a given DataFrame.
# - The `.shape` attribute of a DataFrame provides a tuple containing (number of rows, number of columns).
# - I convert this tuple into a list to match the required output format.

# Explanation:
# - The `shape` attribute of a DataFrame returns a tuple (rows, columns).
# - By converting this tuple into a list, I ensure the return type is `[rows, columns]` as required.
# - This approach is efficient and directly provides the needed information.
