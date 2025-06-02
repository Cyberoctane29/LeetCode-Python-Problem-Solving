# Problem 596: Classes With at Least 5 Students
# Difficulty: Easy

# Table: Courses
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class) is the primary key (combination of unique values).
# Each row indicates a student's enrollment in a class.

# Problem:
# Write a function to find all the classes that have at least five students.
# Return the result table in any order.

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # I count how many students are in each class
    student_counts = courses['class'].value_counts()

    # I filter to keep only those classes with more than 5 students
    filtered_counts = student_counts.loc[student_counts >= 5]

    # I convert the result to a DataFrame and rename columns
    result_df = filtered_counts.reset_index().rename(columns={'index': 'class'})

    # I return only the 'class' column as required
    return result_df[['class']]

# Intuition:
# - I need to count the number of students in each class.
# - Then, I pick out the classes where that count is at least 5.
# - Finally, I format the result as a DataFrame containing just the class names.

# Explanation:
# - I use `value_counts()` to get the count of students in each class.
# - I filter for counts >= 5.
# - I reset the index to turn the Series into a DataFrame and rename the index to 'class'.
# - I select and return only the 'class' column as per the problem requirement.
