# Problem 3421: Find Students Who Improved
# Difficulty: Medium

# Table: Scores
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student_id  | int     |
# | subject     | varchar |
# | score       | int     |
# | exam_date   | varchar |
# +-------------+---------+
# (student_id, subject, exam_date) is the primary key.

# Problem Statement:
# Write a function to find students who have shown improvement.
# A student is considered to have improved if:
# - They have taken exams in the same subject on at least two different dates.
# - Their latest score in that subject is higher than their first score.
# Return the result table ordered by student_id, subject in ascending order.

# Solution 1

import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    # I sort the table by student_id, subject, exam_date so that first and last exams align naturally
    temp_df = scores.sort_values(by=['student_id', 'subject', 'exam_date'])

    # I compute first and latest scores by grouping and using 'first' and 'last'
    temp_df1 = temp_df.groupby(['student_id', 'subject'], as_index=False).agg(
        first_score=('score', 'first'),
        latest_score=('score', 'last')
    )

    # I filter out records where the latest score is higher than the first
    result_df = temp_df1[temp_df1['first_score'] < temp_df1['latest_score']]

    # I return the final result
    return result_df

# Intuition:
# I need to compare the first and latest exam scores for each student in each subject and check if the latest score improved.

# Explanation:
# I first sort the scores by student, subject, and exam date.
# Then, I group by student and subject to get the first and last scores using 'first' and 'last'.
# After that, I filter where the latest score is higher than the first and return this result.

# Solution 2

import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    # I group by student_id and subject, then compute first and latest scores by date comparison
    temp_df = scores.groupby(['student_id', 'subject'], as_index=False).apply(
        lambda x: pd.Series({
            'first_score': x[x['exam_date'] == x['exam_date'].min()]['score'].iloc[0],
            'latest_score': x[x['exam_date'] == x['exam_date'].max()]['score'].iloc[0]
        })
    )

    # I filter where the latest score is higher than the first and sort the result
    result_df = temp_df.loc[
        (temp_df['first_score'] < temp_df['latest_score'])
    ].sort_values(by=['student_id', 'subject'], ascending=[True, True])

    # I return the final result
    return result_df

# Intuition:
# Similar to Solution 1 — but I explicitly select scores on the earliest and latest exam dates for each student and subject.

# Explanation:
# I group by student_id and subject, then for each group, find the score on the earliest and latest exam dates.
# I construct a new DataFrame with these values.
# Finally, I filter where the latest score is higher than the first, sort by student_id and subject, and return the result.
