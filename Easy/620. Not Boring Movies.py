# Problem 620: Not Boring Movies
# Difficulty: Easy

# Table: Cinema
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | id             | int      |
# | movie          | varchar  |
# | description    | varchar  |
# | rating         | float    |
# +----------------+----------+
# id is the primary key for this table.
# Each row contains information about a movie's name, description, and rating.

# Problem Statement:
# I need to write a solution to return movies with an odd-numbered id and a description that is not 'boring'.
# The result should be ordered by rating in descending order.

# Solution 1

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # I apply a boolean mask to filter movies with an odd id and description not equal to 'boring'
    # I then sort the filtered result by rating in descending order
    return cinema.loc[
        (cinema['id'] % 2 != 0) & (cinema['description'] != 'boring'), :
    ].sort_values(by='rating', ascending=False)

# Intuition for Solution 1:
# - I need to select movies whose id is odd and description isn't 'boring'.
# - I use boolean filtering to achieve this directly with Pandas' `loc`.
# - I finally sort the result by rating in descending order.

# Explanation for Solution 1:s
# - I apply a boolean mask to filter rows with odd ids and non-'boring' descriptions.
# - I then sort the filtered result by rating using `sort_values()` in descending order.


# Solution 2

import pandas as pd 

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # I handle the case where the input DataFrame might be empty
    if cinema.empty:
        return cinema
    
    filtered_df = []
    # I iterate through each row of the DataFrame
    for index, movie in cinema.iterrows():
        # I check if the movie has an odd id and a description that is not 'boring'
        if (movie['id'] % 2 != 0) and (movie['description'] != 'boring'):
            # I collect the ids of movies that meet both conditions
            filtered_df.append(movie['id'])
    # I filter the original DataFrame based on collected ids and sort by rating in descending order
    return cinema[cinema['id'].isin(filtered_df)].sort_values(by='rating', ascending=False)

# Intuition for Solution 2:
# - I manually iterate through each movie to check the required conditions.
# - I collect the ids of movies meeting both conditions.
# - I filter the original DataFrame using these ids and sort by rating.

# Explanation for Solution 2:
# - I iterate over the rows using `iterrows()` and check both conditions.
# - I collect the ids of qualifying movies.
# - I filter the original DataFrame using these ids.
# - I sort the final result by rating in descending order.


# Solution 3

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # I apply a boolean mask to select movies with an odd id and description not equal to 'boring'
    # I then sort the filtered DataFrame by rating in descending order
    return cinema[
        (cinema['id'] % 2 != 0) & (cinema['description'] != 'boring')
    ].sort_values(by='rating', ascending=False)

# Intuition for Solution 3:
# - I use direct boolean filtering to select the required movies.
# - I sort the final result by rating in descending order.
# - This keeps the solution clean and efficient.

# Explanation for Solution 3:
# - I apply a boolean mask to select movies meeting both conditions.
# - I sort the filtered DataFrame by rating using `sort_values()` in descending order.
# - This results in a concise and efficient solution.
