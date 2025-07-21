# Problem 3451: Find Invalid IP Addresses
# Difficulty: Hard

# Table: logs
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | log_id      | int     |
# | ip          | varchar |
# | status_code | int     |
# +-------------+---------+
# log_id is the unique key for this table.
# Each row contains server access log information including IP address and HTTP status code.

# Problem Statement:
# Write a function to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:
# - Contains numbers greater than 255 in any octet
# - Has leading zeros in any octet (like 01.02.03.04)
# - Has less or more than 4 octets
# Return the result table ordered by invalid_count and ip in descending order respectively.

# Solution 1

import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    # I define a helper function to check if an IP is invalid
    def invalid_ips(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return True
        flag1 = any(int(octet) > 255 for octet in parts)
        flag2 = any(octet.startswith('0') for octet in parts if octet != '0')
        return flag1 or flag2

    # I apply the helper function to create a new column flagging invalid IPs
    logs['invalid_flag'] = logs['ip'].apply(invalid_ips)
    
    # I filter only invalid IPs
    temp_df = logs[logs['invalid_flag'] == 1]
    
    # I group by IP and count the number of occurrences
    result_df = temp_df.groupby('ip', as_index=False).agg(invalid_count=('ip', 'count'))
    
    # I sort the result as per requirements
    return result_df.sort_values(by=['invalid_count', 'ip'], ascending=[False, False])

# Intuition:
# I parse each IP into octets and apply validation rules:
# - Number of octets = 4
# - No octet should exceed 255
# - No leading zeros (unless the octet is exactly "0")

# Explanation:
# I split the IP string into its four components and validate each part using the rules provided.
# If any rule fails, I flag it as invalid.
# Then I count how many times each invalid IP appears and sort the final result accordingly.

# Solution 2

import pandas as pd
import re

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    # I define a regex pattern for valid IPv4 addresses
    pattern = r'^((25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]?\d)$'
    
    # I filter IPs that do not match the pattern
    invalid_ips = logs[~logs['ip'].str.match(pattern)]
    
    # I group the invalid IPs and count their occurrences
    result_df = invalid_ips.groupby('ip', as_index=False).agg(invalid_count=('ip', 'count'))
    
    # I return the result sorted as required
    return result_df.sort_values(by=['invalid_count', 'ip'], ascending=[False, False])

# Intuition:
# I use a regular expression to define a valid IPv4 address and filter out anything that doesn’t match it.

# Explanation:
# The regex ensures:
# - Exactly four numeric octets separated by dots
# - Each octet is between 0 and 255
# - No leading zeros in multi-digit numbers
# I filter rows failing this pattern, group by IP, count occurrences, and return the sorted result.
