# Problem 1050: Actors and Directors Who Cooperated At Least Three Times
# Difficulty: Easy

# Table: ActorDirector
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key for this table.
# Each row records a cooperation instance between an actor and a director.

# Problem Statement:
# Write a solution to find all actor-director pairs that have worked together at least three times.
# The result can be returned in any order.

# Solution 1

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # I group the records by actor_id and director_id and count the number of records for each pair
    temp_df = actor_director.groupby(by=['actor_id', 'director_id'], as_index=False).size()
    # I filter out the pairs where the count is at least 3
    return temp_df.loc[temp_df['size'] >= 3, ['actor_id', 'director_id']]

# Intuition for Solution 1:
# - I need to count how many times each actor-director pair appears.
# - I use `groupby` on both actor_id and director_id and count the occurrences.
# - I filter the groups where the count is 3 or more and select the actor_id and director_id columns.

# Explanation for Solution 1:
# - I use `groupby` to cluster records by actor-director pair.
# - I count the number of times each pair appears using `size()`.
# - I filter for those pairs where the count is at least 3.
# - I return the actor_id and director_id columns for those qualifying pairs.


# Solution 2

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # I group the records and count the size for each actor-director pair
    # I use a lambda function to filter those with a size of at least 3
    return actor_director.groupby(by=['actor_id', 'director_id'], as_index=False).size()\
        .loc[lambda x: x['size'] >= 3, ['actor_id', 'director_id']]

# Intuition for Solution 2:
# - I perform the same grouping and counting as Solution 1.
# - I use a lambda function with `loc` to directly filter out pairs where the count is at least 3.

# Explanation for Solution 2:
# - I group by actor_id and director_id and count occurrences.
# - I apply a lambda function in `loc` to filter rows with a count of at least 3.
# - I select and return only the actor_id and director_id columns.


# Solution 3

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # I group the records and count the occurrences for each actor-director pair
    # I use the query() method to filter for pairs with a size of at least 3
    return actor_director.groupby(by=['actor_id', 'director_id'], as_index=False).size()\
        .query("size >= 3")[['actor_id', 'director_id']]

# Intuition for Solution 3:
# - I use the same grouping and counting logic.
# - I use Pandas' `query()` method for a clean, readable way to filter pairs based on the count.

# Explanation for Solution 3:
# - I group and count the number of records per actor-director pair.
# - I use `query()` to select only those with a count of at least 3.
# - I return the actor_id and director_id columns from the filtered result.
