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
# I need to create a record for every possible student-subject combination.
# Then, for each combination, I need to count how many times the student attended the exam for that subject.
# If a student didn’t attend a particular exam, I should treat the attendance count as zero.

# Explanation:
# I start by performing a cross join between the Students and Subjects tables to create all possible student-subject pairs.
# Next, I group the Examinations table by student_id and subject_name and count the number of attendance records for each pair.
# I merge these attendance counts with the complete list of student-subject pairs to ensure every possible combination is represented.
# I replace any missing attendance counts with zero since not every student attended every exam.
# Finally, I sort the result by student_id and subject_name before returning it.
