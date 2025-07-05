# Problem 1341: Movie Rating
# Difficulty: Medium

# Table: Movies
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | title         | varchar |
# +---------------+---------+
# movie_id is the primary key (column with unique values) for this table.
# title is the name of the movie.

# Table: Users
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# The column 'name' has unique values.

# Table: MovieRating
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | user_id       | int     |
# | rating        | int     |
# | created_at    | date    |
# +---------------+---------+
# (movie_id, user_id) is the primary key (column with unique values) for this table.
# This table contains the rating of a movie by a user in their review.
# created_at is the user's review date.

# Problem Statement:
# Write a function to:
# - Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
# - Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

# Solution

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # I count the number of movies rated by each user
    temp_df1 = movie_rating.groupby('user_id', as_index=False).agg(user_count=('user_id', 'count'))
    
    # I merge this count with the users table to get their names
    merged_df1 = pd.merge(temp_df1, users, how='left', on='user_id').sort_values(
        by=['user_count', 'name'], ascending=[False, True]
    ).head(1)
    
    # I filter the movie_rating table for reviews created in February 2020
    movie_rating_feb = movie_rating.loc[
        (movie_rating['created_at'].dt.month == 2) & (movie_rating['created_at'].dt.year == 2020), 
    ]
    
    # I calculate the average rating for each movie in that period
    temp_df2 = movie_rating_feb.groupby('movie_id', as_index=False).agg(rating_average=('rating', 'mean'))
    
    # I merge these averages with the movies table to get the titles
    merged_df2 = pd.merge(temp_df2, movies, how='left', on='movie_id').sort_values(
        by=['rating_average', 'title'], ascending=[False, True]
    ).head(1)
    
    # I return both results combined in a single column DataFrame
    return pd.DataFrame({'results': pd.concat([merged_df1['name'], merged_df2['title']])})

# Intuition:
# I need to find:
# 1. The most active reviewer based on count and break ties by name.
# 2. The movie with the highest average rating in February 2020 and break ties by title.

# Explanation:
# I first group movie_rating by 'user_id' and count the ratings.
# Then, I merge this with the users table and sort by rating count and name to get the top reviewer.
# For the second part, I filter movie_rating for February 2020, compute average ratings per movie, and merge with the movies table.
# I then sort by average rating and title to find the top movie.
# Finally, I concatenate both results into a single DataFrame for output.
