# Problem 2877: Create a DataFrame from List
# Difficulty: Easy

# Problem Statement:
# Write a function to create a DataFrame from a 2D list called student_data. 
# This 2D list contains the IDs and ages of some students.
# The DataFrame should have two columns, 'student_id' and 'age', and maintain the same order as the original list.

# Solution 1

import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_id, age = zip(*student_data)
    return pd.DataFrame({'student_id': student_id, 'age': age})

# Intuition:
# - I need to convert a 2D list into a structured DataFrame.
# - The data consists of student IDs and their corresponding ages.
# - I unpack the list into two separate tuples using `zip()`, then create the DataFrame.

# Explanation:
# - I use `zip(*student_data)` to separate student IDs and ages into individual sequences.
# - A dictionary is created with 'student_id' and 'age' as keys, mapping to their respective values.
# - The dictionary is passed to `pd.DataFrame()` to construct the required DataFrame.

# Solution 2

import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

# Intuition:
# - I need to create a DataFrame while preserving the order of the input 2D list.
# - Since the input already follows the required format, I can directly convert it into a DataFrame.

# Explanation:
# - I pass `student_data` directly to `pd.DataFrame()` while specifying the column names.
# - This ensures the resulting DataFrame maintains the same order and structure as the input list.
