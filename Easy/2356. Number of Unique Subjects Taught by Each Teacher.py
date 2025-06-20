# Problem 2356: Number of Unique Subjects Taught by Each Teacher
# Difficulty: Easy

# Table: Teacher
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | teacher_id  | int  |
# | subject_id  | int  |
# | dept_id     | int  |
# +-------------+------+
# (subject_id, dept_id) is the primary key (combination of columns with unique values) for this table.
# Each row indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

# Problem Statement:
# Write a function to calculate the number of unique subjects each teacher teaches in the university.
# Return the result table in any order.

# Solution

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # I group the table by teacher_id and count the number of unique subject_id values for each teacher
    result_df = teacher.groupby('teacher_id', as_index=False).agg(cnt=('subject_id', 'nunique'))
    
    # I return the resulting DataFrame
    return result_df

# Intuition:
# I need to count how many distinct subjects each teacher handles.
# To achieve this, I will group the data by teacher_id and count the unique subject_id values in each group.

# Explanation:
# I use groupby on the teacher_id to group records by each teacher.
# Then, I use nunique on the subject_id column to count the distinct subjects a teacher teaches.
# I reset the index to keep teacher_id as a column and rename the count column as 'cnt'.
# Finally, I return the resulting DataFrame.
