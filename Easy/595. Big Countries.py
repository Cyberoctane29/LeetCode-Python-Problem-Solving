# Problem 595: Big Countries
# Difficulty: Easy

# Table: World
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | bigint  |
# +-------------+---------+
# name is the primary key (column with unique values) for this table.
# Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

# Problem Statement:
# A country is big if:
# - It has an area of at least three million (i.e., 3000000 km²), or
# - It has a population of at least twenty-five million (i.e., 25000000).
# Write a function to find the name, population, and area of the big countries.
# Return the result table in any order.

# Solution

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ['name', 'population', 'area']]

# Intuition:
# - I need to filter the countries that have an area of at least 3,000,000 km² or a population of at least 25,000,000.
# - The filtered countries should display only the `name`, `population`, and `area`.

# Explanation:
# - `world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000)]` selects countries that meet at least one of the conditions.
# - `[['name', 'population', 'area']]` ensures that only the required columns are returned.
