# Problem 3475: DNA Pattern Recognition
# Difficulty: Medium

# Table: Samples
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | sample_id      | int     |
# | dna_sequence   | varchar |
# | species        | varchar |
# +----------------+---------+
# sample_id is the unique key for this table.

# Problem Statement:
# Write a function to identify sample_id for sequences that:
# - Start with 'ATG'
# - End with one of 'TAA', 'TAG', 'TGA'
# - Contain 'ATAT'
# - Have at least 3 consecutive 'G'

# Return the result table ordered by sample_id ascending.

# Solution 1

import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    # I create a new column for each pattern, checking the condition and converting boolean to int (0/1)
    samples['has_start'] = samples['dna_sequence'].str.startswith('ATG').astype(int)
    samples['has_stop']  = samples['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA')).astype(int)
    samples['has_atat']  = samples['dna_sequence'].str.contains('ATAT').astype(int)
    samples['has_ggg']   = samples['dna_sequence'].str.contains('GGG').astype(int)

    # I return the result sorted by sample_id
    return samples.sort_values('sample_id')

# Intuition:
# I need to detect specific string patterns in DNA sequences for each sample and mark them as 1 (present) or 0 (absent).

# Explanation:
# I use pandas string methods to check if each sequence starts with 'ATG', ends with one of the stop codons, contains 'ATAT', or contains 'GGG'.
# I convert these boolean results to integers and add them as new columns.
# Finally, I sort the table by sample_id and return it.

# Solution 2

import pandas as pd
import numpy as np

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    # I use .assign() with lambda expressions and np.where to generate new columns based on pattern matches
    result_df = samples.assign(
        has_start = lambda x: np.where(x['dna_sequence'].str.startswith('ATG'), 1, 0),
        has_stop  = lambda x: np.where(x['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA')), 1, 0),
        has_atat  = lambda x: np.where(x['dna_sequence'].str.contains('ATAT'), 1, 0),
        has_ggg   = lambda x: np.where(x['dna_sequence'].str.contains('GGG'), 1, 0)
    ).sort_values(by='sample_id')

    # I return the final result
    return result_df

# Intuition:
# Similar goal as Solution 1 — detect DNA sequence patterns and label them with 1 or 0, but using .assign() and np.where for a cleaner, one-shot approach.

# Explanation:
# I use the .assign() method combined with lambda functions and np.where to add new columns indicating the presence of each pattern.
# Each lambda checks the pattern in the dna_sequence and assigns 1 if present, 0 if not.
# I then sort by sample_id and return the final DataFrame.
