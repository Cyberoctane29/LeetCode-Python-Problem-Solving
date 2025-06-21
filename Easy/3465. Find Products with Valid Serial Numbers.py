# Problem 3465: Find Products with Valid Serial Numbers
# Difficulty: Easy

# Table: products
# +--------------+------------+
# | Column Name  | Type       |
# +--------------+------------+
# | product_id   | int        |
# | product_name | varchar    |
# | description  | varchar    |
# +--------------+------------+
# product_id is the unique key for this table.
# Each row in the table represents a product with its unique ID, name, and description.

# Problem Statement:
# Write a function to find all products whose description contains a valid serial number.
# A valid serial number must:
# - Start with the uppercase letters 'SN'.
# - Be followed by exactly 4 digits.
# - Then have a hyphen (-).
# - And finally followed by exactly 4 digits.
# The serial number can appear anywhere in the description.
# Return the result table ordered by product_id in ascending order.

# Solution

import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    # I use str.contains() with a regex pattern to detect valid serial numbers in the description
    result_df = products[products['description'].str.contains(r"\bSN[0-9]{4}-[0-9]{4}\b", regex=True)]
    
    # I sort the result by product_id as required
    return result_df.sort_values(by='product_id')

# Intuition:
# I need to identify product descriptions containing a serial number in a strict format.
# Using a regular expression is the simplest and most reliable way to match such structured patterns in text.

# Explanation:
# I use a regex pattern `\bSN[0-9]{4}-[0-9]{4}\b`:
# - `\b` asserts a word boundary to ensure correct matching.
# - `SN` matches the uppercase letters 'SN'.
# - `[0-9]{4}` matches exactly 4 digits.
# - `-` matches a hyphen.
# - `[0-9]{4}` matches another set of exactly 4 digits.
# - Another `\b` ensures the serial number is a complete token, not part of a larger string.
# I use str.contains() with this regex on the 'description' column to filter relevant rows.
# I then sort the result by 'product_id' in ascending order and return the final DataFrame.
