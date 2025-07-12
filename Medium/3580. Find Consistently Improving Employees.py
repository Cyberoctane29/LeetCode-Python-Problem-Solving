# Problem 3580: Find Consistently Improving Employees
# Difficulty: Medium

# Table: employees
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# +-------------+---------+

# Table: performance_reviews
# +-------------+------+ 
# | Column Name | Type |
# +-------------+------+
# | review_id   | int  |
# | employee_id | int  |
# | review_date | date |
# | rating      | int  |
# +-------------+------+

# Problem Statement:
# Write a function to find employees with at least 3 reviews whose last 3 performance ratings are strictly increasing.
# Use the most recent 3 reviews (by date) for each employee.
# Calculate improvement score as (latest rating - earliest rating) within those 3.
# Return result ordered by improvement_score descending, then by name ascending.

# Solution

import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    # I define a helper function to check if an employee's last 3 ratings are strictly increasing
    def if_improving(group):
        if len(group) >= 3:
            a, b, c = group.iloc[-3:]
            if (a < b) & (b < c):
                return True
            else:
                return False
        else:
            return False

    # I sort reviews by employee and review_date so latest 3 reviews are at the end
    performance_reviews = performance_reviews.sort_values(by=['employee_id', 'review_date'], ascending=[True, True])

    # I apply the helper function to each employee's ratings and identify those improving
    rating_improv_flag = performance_reviews.groupby('employee_id')['rating'].apply(if_improving)
    valid_users = rating_improv_flag[rating_improv_flag].index

    # I filter reviews to only those improving employees
    temp_df = performance_reviews[performance_reviews['employee_id'].isin(valid_users)]

    # I compute improvement score as (latest - earliest) from last 3 ratings per employee
    temp_df1 = temp_df.groupby('employee_id', as_index=False).agg(
        improvement_score=('rating', lambda x: x.iloc[-1] - x.iloc[-3])
    )

    # I merge with employee names and sort as required
    result_df = temp_df1.merge(employees, how='left', on='employee_id').sort_values(
        by=['improvement_score', 'name'], ascending=[False, True]
    )

    # I select final required columns
    return result_df[['employee_id', 'name', 'improvement_score']]

# Intuition:
# I first check if each employee has at least 3 reviews and if their latest 3 ratings form a strictly increasing sequence.
# If yes, I calculate the improvement score as the difference between the last and first ratings among those 3.
# Then I merge with employee names and sort based on improvement score (descending) and name (ascending).

# Explanation:
# The main idea is to process each employee's reviews in date order and verify their last 3 ratings.
# I identify employees meeting the increasing trend condition, then compute improvement scores using positional indexing.
# Finally, I join employee details and organize the final output according to the problem's sorting rules.
