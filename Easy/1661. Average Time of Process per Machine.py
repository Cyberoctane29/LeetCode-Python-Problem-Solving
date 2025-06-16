# Problem 1661: Average Time of Process per Machine
# Difficulty: Easy

# Table: Activity
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | machine_id     | int     |
# | process_id     | int     |
# | activity_type  | enum    |
# | timestamp      | float   |
# +----------------+---------+
# (machine_id, process_id, activity_type) is the primary key of this table.
# The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
# It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.

# Problem Statement:
# Write a function to find the average time each machine takes to complete a process.
# The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
# The average time is calculated by the total time to complete every process on the machine divided by the number of processes run.
# The resulting table should have the machine_id along with the average time as processing_time, rounded to 3 decimal places.
# Return the result table in any order.

# Solution 1

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # I reshape the Activity table to create separate 'start' and 'end' columns for each (machine_id, process_id)
    pivot_df = activity.pivot(index=['machine_id', 'process_id'], columns='activity_type', values='timestamp').reset_index()
    
    # I calculate the processing time for each process by subtracting 'start' from 'end'
    pivot_df['processing_time'] = pivot_df['end'] - pivot_df['start']
    
    # I compute the average processing time for each machine and round to 3 decimal places
    result_df = pivot_df.groupby('machine_id', as_index=False).agg(
        processing_time=('processing_time', lambda x: round(x.mean(), 3))
    )
    
    # I return the final result
    return result_df

# Intuition:
# I need to compute the time taken for each (machine_id, process_id) by subtracting the 'start' timestamp from the 'end' timestamp.
# After that, I will calculate the average of these processing times for each machine.
# This requires reshaping the table so that both 'start' and 'end' timestamps appear in separate columns.

# Explanation:
# I start by reshaping the Activity table using pivot() to separate 'start' and 'end' timestamps into columns for each (machine_id, process_id).
# Then, I calculate the processing time by subtracting 'start' from 'end' for each process.
# Next, I group the data by machine_id and compute the mean of the processing times.
# I round the resulting average to 3 decimal places.
# Finally, I return a DataFrame with machine_id and processing_time.

# Solution 2

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # I compute the processing time for each (machine_id, process_id) by subtracting the 'start' timestamp from the 'end' timestamp
    pivot_df = activity.groupby(['machine_id', 'process_id']).apply(
        lambda df: df.loc[df['activity_type'] == 'end', 'timestamp'].values[0] -
                   df.loc[df['activity_type'] == 'start', 'timestamp'].values[0]
    ).reset_index(name='processing_time')
    
    # I compute the average processing time for each machine and round to 3 decimal places
    result_df = pivot_df.groupby('machine_id', as_index=False).agg(
        processing_time=('processing_time', lambda x: round(x.mean(), 3))
    )
    
    # I return the final result
    return result_df

# Intuition:
# I need to compute the processing time for each (machine_id, process_id) by subtracting the 'start' timestamp from the 'end' timestamp.
# Instead of reshaping the table, I can group the records for each (machine_id, process_id) and directly compute the difference.
# Then, I will compute the average of these processing times for each machine.

# Explanation:
# I group the Activity table by machine_id and process_id.
# Within each group, I locate the 'end' and 'start' timestamps and subtract them to get the processing time.
# I reset the index and name the resulting column as 'processing_time'.
# Then, I group this result by machine_id and compute the average of the processing times.
# I round the average to 3 decimal places and return the resulting DataFrame with machine_id and processing_time.
