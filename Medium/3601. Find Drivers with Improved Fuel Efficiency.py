# Problem 3601: Find Drivers with Improved Fuel Efficiency
# Difficulty: Medium

# Table: drivers
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | driver_id   | int     |
# | driver_name | varchar |
# +-------------+---------+

# Table: trips
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | trip_id       | int     |
# | driver_id     | int     |
# | trip_date     | date    |
# | distance_km   | decimal |
# | fuel_consumed | decimal |
# +---------------+---------+

# Problem Statement:
# Write a function to identify drivers whose fuel efficiency improved from the first half of the year (January–June) to the second half (July–December).
# - Calculate fuel efficiency as (distance_km / fuel_consumed) for each trip.
# - Only include drivers with trips in both halves of the year.
# - Compute average fuel efficiency for each half per driver.
# - Compute efficiency improvement as (second_half_avg - first_half_avg).
# - Round all numeric results to 2 decimal places.
# - Return result ordered by efficiency improvement descending, then driver_name ascending.

# Solution 1

import pandas as pd
import numpy as np

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['trip_date'] = pd.to_datetime(trips['trip_date'])
    trips['half'] = np.where(trips['trip_date'].dt.month <= 6, 'H1', 'H2')

    valid_drivers = trips.groupby('driver_id')['half'].nunique()
    valid_drivers = valid_drivers[valid_drivers == 2].index

    temp_df = trips[trips['driver_id'].isin(valid_drivers)]

    result_df = temp_df.groupby('driver_id', as_index=False).apply(
        lambda x: pd.Series({
            'first_half_avg': ((x.loc[x['half'] == 'H1', 'distance_km']) / (x.loc[x['half'] == 'H1', 'fuel_consumed'])).mean(),
            'second_half_avg': ((x.loc[x['half'] == 'H2', 'distance_km']) / (x.loc[x['half'] == 'H2', 'fuel_consumed'])).mean()
        })
    )

    result_df['efficiency_improvement'] = result_df['second_half_avg'] - result_df['first_half_avg']

    result_df = result_df.merge(drivers, how='left', on='driver_id')

    result_df = result_df[result_df['efficiency_improvement'] >= 0].round(2)

    return result_df.sort_values(by=['efficiency_improvement', 'driver_name'], ascending=[False, True])[['driver_id','driver_name','first_half_avg','second_half_avg','efficiency_improvement']]

# Intuition:
# I first categorize trips into H1 or H2 based on trip_date. 
# Then, I identify drivers who have trips in both halves.
# For each such driver, I compute average fuel efficiency in H1 and H2.
# I compute efficiency improvement as the difference and keep only drivers with positive improvement.
# Finally, I merge driver names, round results, and sort by improvement and driver_name.

# Explanation:
# The logic relies on partitioning trips into halves, filtering for drivers with complete year coverage, 
# and calculating per-half average efficiencies via grouped means.
# I use apply with a custom Series for clarity in solution 1.
# Results are ordered by improvement descending and driver_name for tie-breaking.

# Solution 2

import pandas as pd
import numpy as np

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['trip_date'] = pd.to_datetime(trips['trip_date'])
    trips['half'] = np.where(trips['trip_date'].dt.month <= 6, 'H1', 'H2')
    trips['efficiency'] = trips['distance_km'] / trips['fuel_consumed']

    valid_drivers = trips.groupby('driver_id')['half'].nunique()
    valid_drivers = valid_drivers[valid_drivers == 2].index

    temp_df = trips[trips['driver_id'].isin(valid_drivers)]

    result_df = temp_df.groupby('driver_id', as_index=False).agg(
        first_half_avg=('efficiency', lambda x: x[temp_df.loc[x.index, 'half'] == 'H1'].mean()),
        second_half_avg=('efficiency', lambda x: x[temp_df.loc[x.index, 'half'] == 'H2'].mean())
    )

    result_df['efficiency_improvement'] = result_df['second_half_avg'] - result_df['first_half_avg']

    result_df = result_df[result_df['efficiency_improvement'] > 0]

    result_df = result_df.merge(drivers, on='driver_id')

    result_df = result_df[['driver_id', 'driver_name', 'first_half_avg', 'second_half_avg', 'efficiency_improvement']]

    return result_df.round(2).sort_values(by=['efficiency_improvement', 'driver_name'], ascending=[False, True])

# Intuition:
# I first compute per-trip fuel efficiency.
# Then, I find drivers with trips in both halves.
# I group by driver_id and compute average efficiency for each half via lambda conditions inside agg.
# I calculate improvement and filter for positive changes.
# Finally, I merge driver names, round values, and sort by improvement and name.

# Explanation:
# The difference from solution 1 is that I precompute efficiency and use lambda conditions inside agg for per-half means.
# This makes solution 2 a little tighter while logically equivalent.
# The rest of the steps — identifying qualifying drivers, computing improvements, merging driver names, and final sorting — remain consistent.
