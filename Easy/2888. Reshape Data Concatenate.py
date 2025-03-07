# Problem 2888: Reshape Data: Concatenate
# Difficulty: Easy

# Problem Statement:
# Write a function to concatenate two DataFrames, `df1` and `df2`, vertically.

# Solution

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    answer = pd.concat([df1, df2])
    return answer

# Intuition:
# - Since `df1` and `df2` have the same columns, I can stack them vertically.
# - Using `pd.concat()`, I merge both DataFrames while preserving the column structure.

# Explanation:
# - `pd.concat([df1, df2])` combines both DataFrames along the default axis (axis=0, i.e., vertically).
# - The function returns the merged DataFrame containing all rows from both input DataFrames.
