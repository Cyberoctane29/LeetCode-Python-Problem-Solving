# Problem 2891: Method Chaining
# Difficulty: Easy

# Table: animals
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | species     | object |
# | age         | int    |
# | weight      | int    |
# +-------------+--------+

# Problem Statement:
# Write a function to list the names of animals that weigh strictly more than 100 kilograms.
# Return the animals sorted by weight in descending order.

# Solution

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

# Intuition:
# - I need to filter the animals whose weight is greater than 100.
# - Then, I sort the remaining animals in descending order based on weight.
# - Finally, I select only the `name` column for the result.

# Explanation:
# - `animals[animals['weight'] > 100]` filters animals weighing more than 100 kg.
# - `.sort_values(by='weight', ascending=False)` sorts them by weight in descending order.
# - `[['name']]` selects only the `name` column for the final output.
