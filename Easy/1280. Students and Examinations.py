# Problem 1280: Students and Examinations
# Difficulty: Easy

# Table: Students
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the primary key.

# Table: Subjects
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# subject_name is the primary key.

# Table: Examinations
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# There is no primary key for this table, and it may contain duplicate rows.
# Each student takes every course listed in the Subjects table.
# Each row in this table indicates that a student attended the exam for a given subject.

# Problem Statement:
# Write a function to find the number of times each student attended each exam.
# Return the result ordered by student_id and subject_name.

# Solution

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Merge Students and Subjects with a cross join to create all possible student-subject combinations
    merged_df1 = pd.merge(students, subjects, how='cross').sort_values(by=['student_id', 'subject_name'], ascending=[True, True])

    # Group the Examinations table by student_id and subject_name and count how many times each exam was attended
    temp_df = examinations.groupby(['student_id', 'subject_name'], as_index=False).agg(attended_exams=('subject_name', 'count'))

    # Merge the complete combinations with the exam attendance counts
    result_df = pd.merge(merged_df1, temp_df, how='left', on=['student_id', 'subject_name'])

    # Replace missing values (students who didn't attend any exam) with 0
    result_df['attended_exams'] = result_df['attended_exams'].fillna(0)

    # Return the final result
    return result_df

# Intuition:
# The task requires creating a record for every possible student-subject combination.
# Then, for each combination, count how many times the student attended the exam for that subject.
# Any missing attendance records should be treated as zero.

# Explanation:
# First, a cross join between Students and Subjects creates all possible student-subject pairs.
# Next, the Examinations table is grouped by student_id and subject_name to count the number of attendance records for each pair.
# The counts are then merged with the full list of student-subject pairs.
# Missing values in attendance counts are filled with zero since not every student attended every exam.
# Finally, the result is sorted by student_id and subject_name before being returned.
