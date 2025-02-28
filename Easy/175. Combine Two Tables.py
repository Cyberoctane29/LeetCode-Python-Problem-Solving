# Problem 175: Combine Two Tables
# Difficulty: Easy

# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | personId    | int     |
# | lastName    | varchar |
# | firstName   | varchar |
# +-------------+---------+
# personId is the primary key (column with unique values) for this table.
# This table contains information about the ID of some persons and their first and last names.

# Table: Address
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | addressId   | int     |
# | personId    | int     |
# | city        | varchar |
# | state       | varchar |
# +-------------+---------+
# addressId is the primary key (column with unique values) for this table.
# Each row of this table contains information about the city and state of one person with ID = personId.

# Problem Statement:
# Write a function to report the first name, last name, city, and state of each person in the Person table.
# If the address of a personId is not present in the Address table, report null instead.
# The result format should match the expected example.

# Solution

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    answer = person.merge(address[['personId', 'city', 'state']], on='personId', how='left')
    return answer[['firstName', 'lastName', 'city', 'state']]

# Intuition:
# - I need to merge the Person table with the Address table based on 'personId'.
# - Since not all persons have addresses, I use a LEFT JOIN (merge with 'how="left"') to ensure all persons are included.
# - If a person does not have an address, their 'city' and 'state' fields should be NULL.

# Explanation:
# - I use the `.merge()` function in pandas to join the two DataFrames on 'personId'.
# - I specify `how="left"` to ensure all records from the 'person' table are retained, even if there's no match in 'address'.
# - I select only the required columns: 'firstName', 'lastName', 'city', and 'state' for the final output.