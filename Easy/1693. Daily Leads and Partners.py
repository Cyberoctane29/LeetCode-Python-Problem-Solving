# Problem 1693: Daily Leads and Partners
# Difficulty: Easy

# Table: DailySales
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | date_id     | date    |
# | make_name   | varchar |
# | lead_id     | int     |
# | partner_id  | int     |
# +-------------+---------+
# There is no primary key for this table. It may contain duplicates.
# This table contains the date, product name, and the IDs of the lead and partner involved in the sale.

# Problem Statement:
# Write a function to find, for each date_id and make_name, the number of distinct lead_id's and distinct partner_id's.
# Return the result table in any order.

# Solution

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # I group the DailySales table by date_id and make_name
    result_df = daily_sales.groupby(['date_id', 'make_name'], as_index=False).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    )
    
    # I return the final result
    return result_df

# Intuition:
# I need to count the number of distinct leads and partners for each combination of date_id and make_name.
# Grouping by these two columns allows me to compute the nunique() counts for both lead_id and partner_id.

# Explanation:
# I group the DailySales DataFrame by date_id and make_name.
# Within each group, I count the number of unique lead_id values using nunique() and store it as unique_leads.
# Similarly, I count the number of unique partner_id values and store it as unique_partners.
# I reset the index by setting as_index=False to keep the grouping columns as regular columns in the result.
# Finally, I return the resulting DataFrame.
