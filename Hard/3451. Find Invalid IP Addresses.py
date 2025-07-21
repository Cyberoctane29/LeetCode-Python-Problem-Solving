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
# Write a function to identify invalid IPv4 addresses based on the following rules:
# - The IP must consist of exactly four octets.
# - Each octet must be between 0 and 255 (inclusive).
# - Octets must not have leading zeros (e.g., "01", "002").
# Return the list of invalid IPs and their corresponding counts as `invalid_count`,
# ordered by `invalid_count` and `ip` in descending order.

# Solution

import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    # I define helper logic to check invalid IPs
    def invalid_ips(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return True
        flag1 = any(int(octet) > 255 for octet in parts)
        flag2 = any(octet.startswith('0') for octet in parts if octet != '0')
        return flag1 or flag2

    # I apply the invalidity check and filter those rows
    logs['invalid_flag'] = logs['ip'].apply(invalid_ips)
    temp_df = logs[logs['invalid_flag'] == 1]

    # I group by IP and count how many times each invalid IP appears
    result_df = temp_df.groupby('ip', as_index=False).agg(invalid_count=('ip', 'count'))

    return result_df.sort_values(by=['invalid_count', 'ip'], ascending=[False, False])

# Intuition:
# I break each IP string into parts using `split('.')`, then validate:
# - If there aren’t exactly 4 parts, it's invalid.
# - If any part > 255, or has leading zeros, it's invalid.
# Finally, I count how often each invalid IP appears.

# Explanation:
# The key is to enforce all three validity rules:
# (1) Exactly 4 octets, (2) each octet ≤ 255, (3) no leading zeros (excluding '0').
# Using `.apply()` with a helper function keeps the logic readable.
# I return IPs with violations, counted and sorted as required.
