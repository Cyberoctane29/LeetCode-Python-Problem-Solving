# Problem 3586: Find COVID Recovery Patients
# Difficulty: Medium

# Table: patients
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | patient_id  | int     |
# | patient_name| varchar |
# | age         | int     |
# +-------------+---------+

# Table: covid_tests
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | test_id     | int     |
# | patient_id  | int     |
# | test_date   | date    |
# | result      | varchar |
# +-------------+---------+

# Problem Statement:
# Write a function to identify COVID recovery patients — those who had at least one positive test followed by a negative test on a later date.
# Calculate the recovery time as the number of days between the first positive test and the first negative test afterward.
# Only include patients who have recovered.
# Return the result ordered by recovery_time ascending, then by patient_name ascending.

# Solution:

import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    def recovery_time_calc(group):
        if len(group) >= 2:
            pos_tests = group.loc[group['result'] == 'Positive', 'test_date']
            if pos_tests.empty:
                return 0
            pos_date = pos_tests.min()
            neg_tests = group.loc[(group['test_date'] > pos_date) & (group['result'] == 'Negative'), 'test_date']
            if neg_tests.empty:
                return 0
            neg_date = neg_tests.min()
            return int((pd.to_datetime(neg_date) - pd.to_datetime(pos_date)).days)
        else:
            return 0

    covid_tests['test_date'] = pd.to_datetime(covid_tests['test_date'])

    cured_patients = covid_tests.groupby('patient_id').apply(recovery_time_calc).reset_index(name='recovery_time')

    result_df = cured_patients[cured_patients['recovery_time'] > 0].merge(patients, how='left', on='patient_id')
    return result_df[['patient_id', 'patient_name', 'age', 'recovery_time']].sort_values(by=['recovery_time', 'patient_name'], ascending=[True, True])

# Intuition:
# I first convert test_date to datetime for reliable date operations.
# Then, for each patient:
# - If they have ≥2 tests, I check for the earliest positive test date.
# - Then, I look for the earliest negative test on a later date.
# - If both exist, I compute the recovery time as the difference in days.
# After processing all patients, I keep only those with a positive recovery time, merge their demographic details, and order the final result.

# Explanation:
# The approach uses groupby + apply to process each patient's test history independently.
# By finding the first positive and first later negative, I calculate the recovery period.
# I filter for valid recoveries and join with patient details.
# The final result is sorted as required — first by recovery time ascending, then by patient name for tie-breaking.
