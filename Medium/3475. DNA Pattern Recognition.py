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
# sample_id is the unique key.

# Problem Statement:
# Write a function to identify DNA sequences having:
# - A start codon: sequences starting with 'ATG'
# - A stop codon: sequences ending with 'TAA', 'TAG', or 'TGA'
# - The motif 'ATAT' present anywhere
# - At least three consecutive G's ('GGG')
# Return the result ordered by sample_id ascending.

# Solution 1

import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    # I check if sequence starts with 'ATG' → has_start
    samples['has_start'] = samples['dna_sequence'].str.startswith('ATG').astype(int)

    # I check if sequence ends with any of the stop codons → has_stop
    samples['has_stop'] = samples['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA')).astype(int)

    # I check if 'ATAT' exists in sequence → has_atat
    samples['has_atat'] = samples['dna_sequence'].str.contains('ATAT').astype(int)

    # I check if 'GGG' exists in sequence → has_ggg
    samples['has_ggg'] = samples['dna_sequence'].str.contains('GGG').astype(int)

    # I return result ordered by sample_id
    return samples.sort_values('sample_id')

# Intuition:
# I need to check for specific string patterns within each DNA sequence and flag them with 1 if present, else 0.

# Explanation:
# I use string methods to check for:
# - Whether the sequence starts with 'ATG'
# - Whether it ends with any stop codon ('TAA', 'TAG', 'TGA')
# - Whether it contains 'ATAT'
# - Whether it contains 'GGG'
# Then, I convert these boolean results to 0/1 integers and return the table sorted by sample_id.

# Solution 2

import pandas as pd
import numpy as np

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    # I create new columns using np.where for each pattern check
    result_df = samples.assign(
        has_start = np.where(samples['dna_sequence'].str.startswith('ATG'), 1, 0),
        has_stop  = np.where(samples['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA')), 1, 0),
        has_atat  = np.where(samples['dna_sequence'].str.contains('ATAT'), 1, 0),
        has_ggg   = np.where(samples['dna_sequence'].str.contains('GGG'), 1, 0)
    )

    # I return result ordered by sample_id
    return result_df.sort_values('sample_id')

# Intuition:
# Same as Solution 1 — but I directly assign the 0/1 values using np.where within an assign() call.

# Explanation:
# I use np.where to check each pattern and assign 1 if true, else 0 for each new column.
# I use str.startswith(), str.endswith(), and str.contains() for pattern checks.
# Then, I return the final table ordered by sample_id.
