# Problem 585: Investments in 2016
# Difficulty: Medium

# Table: Insurance

# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | pid         | int   |
# | tiv_2015    | float |
# | tiv_2016    | float |
# | lat         | float |
# | lon         | float |
# +-------------+-------+
# pid is the primary key (column with unique values) for this table.
# Each row of this table contains information about one policy where:
# pid is the policyholder's policy ID.
# tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
# lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
# lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.

# Problem Statement:
# Write a function to report the sum of all total investment values in 2016 tiv_2016,
# for all policyholders who:
# - have the same tiv_2015 value as one or more other policyholders, and
# - are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.

# Solution

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # I create a column counting how many times each tiv_2015 value appears
    insurance['tiv_2015_cnt'] = insurance.groupby('tiv_2015')['tiv_2015'].transform('count')
    
    # I create another column counting how many times each (lat, lon) pair appears
    insurance['latlon_pair_cnt'] = insurance.groupby(['lat', 'lon'])['pid'].transform('count')
    
    # I filter to records where tiv_2015 is shared by at least one other policyholder
    # and (lat, lon) is unique
    temp_df = insurance.loc[(insurance['tiv_2015_cnt'] > 1) & (insurance['latlon_pair_cnt'] == 1), ]
    
    # I compute and return the sum of tiv_2016 rounded to 2 decimal places
    result_df = pd.DataFrame({'tiv_2016': [round(temp_df['tiv_2016'].sum(), 2)]})
    return result_df

# Intuition:
# I need to sum the 2016 investment values (tiv_2016) for only those policyholders
# who share their 2015 investment value with others but live in a unique (lat, lon) location.

# Explanation:
# First, I use `groupby().transform('count')` to calculate how many times each tiv_2015 value occurs.
# Then, I check for uniqueness of (lat, lon) by counting how many policyholders are in each city.
# The condition is to keep only those with tiv_2015 repeated more than once and (lat, lon) seen exactly once.
# After filtering, I compute the sum of tiv_2016 for these filtered rows and round the result to two decimal places.
# Problem 585: Investments in 2016
# Difficulty: Medium

# Table: Insurance

# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | pid         | int   |
# | tiv_2015    | float |
# | tiv_2016    | float |
# | lat         | float |
# | lon         | float |
# +-------------+-------+
# pid is the primary key (column with unique values) for this table.
# Each row of this table contains information about one policy where:
# pid is the policyholder's policy ID.
# tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
# lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
# lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.

# Problem Statement:
# Write a function to report the sum of all total investment values in 2016 tiv_2016,
# for all policyholders who:
# - have the same tiv_2015 value as one or more other policyholders, and
# - are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.

# Solution

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # I create a column counting how many times each tiv_2015 value appears
    insurance['tiv_2015_cnt'] = insurance.groupby('tiv_2015')['tiv_2015'].transform('count')
    
    # I create another column counting how many times each (lat, lon) pair appears
    insurance['latlon_pair_cnt'] = insurance.groupby(['lat', 'lon'])['pid'].transform('count')
    
    # I filter to records where tiv_2015 is shared by at least one other policyholder
    # and (lat, lon) is unique
    temp_df = insurance.loc[(insurance['tiv_2015_cnt'] > 1) & (insurance['latlon_pair_cnt'] == 1), ]
    
    # I compute and return the sum of tiv_2016 rounded to 2 decimal places
    result_df = pd.DataFrame({'tiv_2016': [round(temp_df['tiv_2016'].sum(), 2)]})
    return result_df

# Intuition:
# I need to sum the 2016 investment values (tiv_2016) for only those policyholders
# who share their 2015 investment value with others but live in a unique (lat, lon) location.

# Explanation:
# First, I use `groupby().transform('count')` to calculate how many times each tiv_2015 value occurs.
# Then, I check for uniqueness of (lat, lon) by counting how many policyholders are in each city.
# The condition is to keep only those with tiv_2015 repeated more than once and (lat, lon) seen exactly once.
# After filtering, I compute the sum of tiv_2016 for these filtered rows and round the result to two decimal places.
