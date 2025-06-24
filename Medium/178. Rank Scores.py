# Problem 178: Rank Scores
# Difficulty: Medium

# Table: Scores
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the score of a game. Score is a floating point value with two decimal places.

# Problem Statement:
# Write a function to rank the scores from highest to lowest.
# If two scores tie, they should have the same rank.
# The next ranking number after a tie should be the next consecutive integer without gaps.
# Return the result ordered by score in descending order.

# Solution

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # I assign ranks to the scores in descending order using the 'dense' method to avoid gaps after ties
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # I select the score and rank columns for the final result
    result_df = scores[['score', 'rank']]
    
    # I sort the result by score in descending order as required
    return result_df.sort_values(by='score', ascending=False)

# Intuition:
# I need to rank the scores from highest to lowest.
# If multiple scores tie, they should have the same rank.
# I will use Pandas' rank() function with the 'dense' method to handle ties and avoid rank gaps.

# Explanation:
# I call rank() on the 'score' column, setting method='dense' to assign the same rank to tied scores and increment ranks consecutively.
# I set ascending=False to rank higher scores first.
# I select the 'score' and 'rank' columns for the result.
# Finally, I sort the result by 'score' in descending order to match the problem requirement.
