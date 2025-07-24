# Problem 3482: Analyze Organization Hierarchy
# Difficulty: Hard

# Table: Employees
# +----------------+---------+
# | Column Name    | Type    | 
# +----------------+---------+
# | employee_id    | int     |
# | employee_name  | varchar |
# | manager_id     | int     |
# | salary         | int     |
# | department     | varchar |
# +----------------+----------+
# employee_id is the unique key for this table.
# Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department.
# manager_id is null for the top-level manager (CEO).

# Problem Statement:
# Write a solution to analyze the organizational hierarchy and answer the following:
# - Hierarchy Levels: For each employee, determine their level in the organization (CEO is level 1, employees reporting directly to the CEO are level 2, and so on).
# - Team Size: For each employee who is a manager, count the total number of employees under them (direct and indirect reports).
# - Salary Budget: For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).
# Return the result table ordered by the result ordered by level in ascending order, then by budget in descending order, and finally by employee_name in ascending order.

# Solution

import pandas as pd
from collections import defaultdict

def analyze_organization_hierarchy(df: pd.DataFrame) -> pd.DataFrame:
                                     
    def traverseGraph(mgr: int, lev: int) -> None:
        # I set the current manager's level
        levl[mgr] = lev
        
        # I traverse through each employee reporting to this manager
        for emp in grph[mgr]:
            traverseGraph(emp, lev + 1)
            
            # I accumulate team size and budget recursively
            team[mgr] += team[emp] + 1
            bdgt[mgr] += bdgt[emp]
        return    

    # I build the manager-to-employee graph
    grph = defaultdict(list)
    levl, team, bdgt = defaultdict(int), defaultdict(int), defaultdict(int)
    
    # I identify the top-level manager (CEO)
    boss = df.loc[df.manager_id.isna(), "employee_id"].values[0]
    
    # I populate the graph and initialize budgets with individual salaries
    for mgr, emp, sal in zip(df.manager_id, df.employee_id, df.salary):
        grph[mgr].append(emp)
        bdgt[emp] = sal   
    
    # I start DFS from the CEO to populate level, team size, and budget
    traverseGraph(boss, 1)

    # I add the computed columns to the DataFrame
    df['level']     = df.employee_id.apply(lambda x: levl[x])
    df['team_size'] = df.employee_id.apply(lambda x: team[x])
    df['budget']    = df.employee_id.apply(lambda x: bdgt[x])

    # I return the final sorted result as per requirements
    return df.sort_values(['level','budget','employee_name'], 
                          ascending=[1,0,1])[['employee_id', 'employee_name', 'level', 'team_size', 'budget']]

# Intuition:
# I need to compute hierarchical information in an organization using a tree-like structure.
# Each manager has direct reports who may themselves be managers, so I use DFS to calculate:
# - level (distance from CEO)
# - team size (number of all employees under a manager)
# - budget (sum of salaries under the manager's control)

# Explanation:
# I create a graph where each manager points to a list of their direct reports.
# I initialize the `budget` dictionary with employees' own salaries and fill in team size and levels via DFS traversal.
# While returning from recursion, I aggregate the budget and team size upward through the tree.
# The final DataFrame gets three new columns: `level`, `team_size`, and `budget`.
# I sort the DataFrame as required by level (asc), budget (desc), and employee_name (asc), and return the required columns.
