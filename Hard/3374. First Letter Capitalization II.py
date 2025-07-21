# Problem 3374: First Letter Capitalization II  
# Difficulty: Hard

# Table: user_content  
# +-------------+---------+  
# | Column Name | Type    |  
# +-------------+---------+  
# | content_id  | int     |  
# | content_text| varchar |  
# +-------------+---------+  
# content_id is the unique key for this table.  
# Each row contains a unique ID and the corresponding text content.

# Problem Statement:
# Write a function to transform the text in the content_text column by applying the following rules:
# - Convert the first letter of each word to uppercase and the remaining letters to lowercase
# - For hyphenated words, capitalize each hyphen-separated part (e.g., "top-rated" → "Top-Rated")
# - Preserve all original spacing and formatting outside the capitalization logic
# Return the original content_text and the modified text in a new column called converted_text.

# Solution

import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    # I capitalize each word while handling hyphenated words separately
    user_content['converted_text'] = user_content['content_text'].apply(
        lambda x: ' '.join(
            ['-'.join([part.capitalize() for part in word.split('-')]) for word in x.split(' ')]
        )
    )
    # I rename the original column for clarity
    result_df = user_content.rename(columns={'content_text': 'original_text'})
    return result_df

# Intuition:
# I apply Python string methods to split text by spaces and hyphens, then capitalize the first letter of each part.
# This lets me handle normal words and hyphenated ones within the same logic.

# Explanation:
# I use `.split()` to break the sentence into words.
# For each word, I further split by hyphen to handle compound terms and capitalize each component using `.capitalize()`.
# Then I join hyphenated parts back, and finally join the words using space.
# The original column is renamed to 'original_text' and the transformed column is added as 'converted_text'.
