# Problem 2887: Fill Missing Data
# Difficulty: Easy

# Problem Statement:
# Write a function to fill missing values in the `quantity` column with 0 in the `products` DataFrame.

# Solution

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

# Intuition:
# - The `quantity` column may contain missing values (NaN), which need to be replaced with 0.
# - I use the `fillna(0)` method to replace NaN values in the `quantity` column.

# Explanation:
# - The `fillna(0)` method ensures that all missing values in the `quantity` column are replaced with 0.
# - The modified DataFrame is returned with no missing values in the `quantity` column.
