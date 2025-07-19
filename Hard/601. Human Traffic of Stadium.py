# Problem 601: Human Traffic of Stadium
# Difficulty: Hard

# Table: Stadium
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | visit_date    | date    |
# | people        | int     |
# +---------------+---------+
# visit_date is the column with unique values for this table.
# Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
# As the id increases, the date increases as well.

# Problem Statement:
# Write a function to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
# Return the result table ordered by visit_date in ascending order.

# Solution 1

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # I filter only the rows where people >= 100, sort by 'id', and reset index
    temp_df = stadium[stadium['people'] >= 100].sort_values(by='id').reset_index(drop=True)
    if temp_df.empty:
        return pd.DataFrame(columns=stadium.columns)

    result = []
    current_seq = [temp_df.loc[0, 'id']]  # I initialize the sequence with the first valid ID

    # I iterate through the filtered DataFrame to detect consecutive ID sequences
    for i in range(1, len(temp_df)):
        if temp_df.loc[i, 'id'] - temp_df.loc[i - 1, 'id'] == 1:
            current_seq.append(temp_df.loc[i, 'id'])
        else:
            if len(current_seq) >= 3:
                result.extend(current_seq)
            current_seq = [temp_df.loc[i, 'id']]

    if len(current_seq) >= 3:
        result.extend(current_seq)
    
    # I extract the original rows using IDs and sort by visit_date
    result_df = stadium[stadium['id'].isin(result)].sort_values(by='visit_date')
    return result_df

# Intuition:
# I first isolate only the rows with people >= 100.
# Then I look for sequences of 3+ consecutive IDs from this filtered set.
# These IDs form the valid rows I must return, ordered by visit_date.

# Explanation:
# I use a sequential loop to check consecutive IDs and collect them into groups.
# Whenever a break in consecutive IDs occurs, I check if the sequence has at least 3 IDs and then add them to the result.
# Finally, I return the matching rows from the original stadium table in order of visit_date.

# Solution 2

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # I filter rows where people >= 100 and sort by 'id'
    stadium = stadium.sort_values('id').query('people >= 100')
    
    # I create a grouping key using index difference trick: id - index
    stadium['id_exp_diff'] = stadium['id'] - range(len(stadium))
    
    # I count the number of IDs in each group to find consecutive blocks
    stadium['n_consec'] = stadium.groupby('id_exp_diff')['id'].transform('count')
    
    # I return only the rows that are part of sequences with at least 3 IDs
    return stadium[stadium.n_consec >= 3][['id', 'visit_date', 'people']]

# Intuition:
# Consecutive IDs have a constant difference with their position index.
# I use that trick to group consecutive rows and then filter groups with length >= 3.

# Explanation:
# I compute a derived key `id - index` and group on it — all rows in a group will have consecutive IDs.
# I use `transform('count')` to tag each row with the size of its group.
# Finally, I return only rows from groups of size 3 or more, selecting just the required columns.
