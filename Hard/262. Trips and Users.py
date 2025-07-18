# Problem 262: Trips and Users
# Difficulty: Hard

# Table: Trips
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | client_id   | int      |
# | driver_id   | int      |
# | city_id     | int      |
# | status      | enum     |
# | request_at  | varchar  |
# +-------------+----------+
# id is the primary key for this table.
# The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
# Status is an ENUM type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

# Table: Users
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | users_id    | int      |
# | banned      | enum     |
# | role        | enum     |
# +-------------+----------+
# users_id is the primary key for this table.
# Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
# banned is an ENUM type of ('Yes', 'No').

# Problem Statement:
# Write a function to compute the cancellation rate of taxi requests where both the client and the driver are not banned.
# The cancellation rate is defined as the number of cancelled (by client or driver) requests divided by the total number of requests with unbanned users on that day.
# Consider only trips between "2013-10-01" and "2013-10-03" inclusive, and only days with at least one valid trip.
# Round the cancellation rate to two decimal places.
# Return the result table with columns `Day` and `Cancellation Rate` in any order.

# Solution 1

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # I filter users by their roles to separate clients and drivers
    clients = users[users["role"] == "client"]
    drivers = users[users["role"] == "driver"]
    
    # I join client and driver information to the trips table
    merged = trips.merge(clients, left_on='client_id', right_on="users_id") \
                  .merge(drivers, left_on='driver_id', right_on="users_id")
    
    # I filter to retain only trips with unbanned clients and drivers, and limit dates
    valid = merged[(merged['banned_x'] == 'No') & (merged['banned_y'] == 'No')]
    valid = valid[valid['request_at'].between('2013-10-01', '2013-10-03')]
    
    # I count total and cancelled trips per day
    total = valid.groupby('request_at').size().rename('total')
    cancelled = valid[valid['status'].isin(['cancelled_by_client', 'cancelled_by_driver'])] \
                    .groupby('request_at').size().rename('cancelled')
    
    # I compute the cancellation rate
    result = pd.concat([total, cancelled], axis=1).fillna(0)
    result['Cancellation Rate'] = (result['cancelled'] / result['total']).round(2)
    
    # I format the output
    result = result.reset_index().rename(columns={'request_at': 'Day'})
    return result[['Day', 'Cancellation Rate']]

# Intuition:
# I need to exclude banned users and then compute the ratio of cancelled trips to total trips per day.
# Grouping by date helps isolate each day’s metrics for this calculation.

# Explanation:
# I first filter users into clients and drivers and join them to the trips table.
# I restrict the dataset to valid (unbanned) users and filter the required date range.
# I count total and cancelled trips per day and compute their ratio.
# Finally, I format and return the DataFrame as required.


# Solution 2

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # I convert 'request_at' to datetime to facilitate date comparisons
    trips['request_at'] = pd.to_datetime(trips['request_at'])

    # I join client data and rename the banned column
    trips = pd.merge(trips, users, how='left', left_on='client_id', right_on='users_id') \
              .rename(columns={'banned': 'clients_banned'})

    # I join driver data and rename the banned column
    trips = pd.merge(trips, users, how='left', left_on='driver_id', right_on='users_id') \
              .rename(columns={'banned': 'drivers_banned'})

    # I filter only unbanned users and restrict dates
    temp_df = trips.loc[
        (trips['clients_banned'] == 'No') &
        (trips['drivers_banned'] == 'No') &
        (trips['request_at'] >= pd.to_datetime('2013-10-01')) &
        (trips['request_at'] <= pd.to_datetime('2013-10-03'))
    ].copy()

    # I flag cancelled trips
    temp_df['is_valid'] = temp_df['status'].str.startswith('cancelled')

    # I calculate the cancellation rate per day
    result_df = temp_df.groupby('request_at', as_index=False).agg(
        Cancellation_Rate=('is_valid', lambda x: round(x.sum() / len(x), 2))
    )

    result_df.columns = ['Day', 'Cancellation Rate']

    return result_df

# Intuition:
# I need to filter to unbanned users and compute cancellation rates per day.
# Converting dates upfront and joining the users table twice allows me to apply these filters effectively.

# Explanation:
# I convert date strings to datetime and perform two left joins to bring in client and driver ban statuses.
# I filter by both ban status and date range.
# Using str.startswith on the status column helps flag cancelled trips.
# I group by date and calculate the proportion of cancellations, rounding to two decimal places.
# The result is formatted and returned.


# Solution 3

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # I convert 'request_at' to datetime
    trips['request_at'] = pd.to_datetime(trips['request_at'])

    # I join user data to get client ban status
    trips = pd.merge(trips, users, how='left', left_on='client_id', right_on='users_id') \
              .rename(columns={'banned': 'clients_banned'})

    # I join user data again to get driver ban status
    trips = pd.merge(trips, users, how='left', left_on='driver_id', right_on='users_id') \
              .rename(columns={'banned': 'drivers_banned'})

    # I restrict the date range
    trips = trips.loc[
        (trips['request_at'] >= pd.to_datetime('2013-10-01')) &
        (trips['request_at'] <= pd.to_datetime('2013-10-03'))
    ]

    # I handle the edge case where there are no trips after filtering
    if trips.empty:
        result_df = pd.DataFrame({'Day': [], 'Cancellation Rate': []})
        return result_df

    # I keep only unbanned clients and drivers
    temp_df = trips.loc[
        (trips['clients_banned'] == 'No') &
        (trips['drivers_banned'] == 'No')
    ]

    # I flag cancelled trips
    temp_df['is_valid'] = temp_df['status'].str.startswith('cancelled')

    # I group by date and calculate the cancellation rate
    result_df = temp_df.groupby('request_at', as_index=False).agg(
        Cancellation_Rate=('is_valid', lambda x: round(x.sum() / len(x), 2))
    )

    result_df.columns = ['Day', 'Cancellation Rate']

    return result_df

# Intuition:
# This solution is similar to Solution 2, but with added safety: it explicitly handles empty DataFrames after filtering.

# Explanation:
# I join the `users` table twice to fetch banned status for both clients and drivers.
# After filtering by both date and banned status, I check if the resulting DataFrame is empty and return an empty result early.
# If data is present, I flag cancelled trips using str.startswith, then compute cancellation rate by grouping by day.
# I format the column names before returning the DataFrame.
