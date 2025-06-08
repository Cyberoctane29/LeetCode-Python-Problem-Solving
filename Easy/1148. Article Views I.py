# Problem 1148: Article Views I
# Difficulty: Easy

# Table: Views
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.

# Problem Statement:
# Write a function to find all the authors that viewed at least one of their own articles.
# Return the result table sorted by id in ascending order.

# Solution

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # I start by filtering rows where the author viewed their own article
    temp = views.loc[views['author_id'] == views['viewer_id'], ['author_id']]
    
    # Then I get the unique author IDs from this filtered data
    # I convert them into a DataFrame with the required column name 'id'
    # Finally, I sort the IDs in ascending order to match the expected output
    answer = pd.DataFrame(temp['author_id'].unique(), columns=['id']).sort_values(by='id')
    
    return answer

# Intuition:
# - I need to find authors who have viewed their own articles.
# - Since `author_id` represents the writer and `viewer_id` represents the person who viewed the article, 
#   an author has viewed their own article if `author_id == viewer_id`.

# Explanation:
# - I filter the DataFrame using `views['author_id'] == views['viewer_id']` to keep only rows where the author viewed their own article.
# - I select only the `author_id` column, since I need unique authors who match the condition.
# - `.unique()` is used to remove duplicates and get distinct author IDs.
# - I create a new DataFrame from these unique IDs and rename the column to `id` as required.
# - Finally, I sort the result in ascending order.
