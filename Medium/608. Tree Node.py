# Problem 608: Tree Node
# Difficulty: Medium

# Table: Tree
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | p_id        | int  |
# +-------------+------+
# id is the column with unique values for this table.
# Each row of this table contains information about the id of a node and the id of its parent node in a tree.
# The given structure is always a valid tree.

# Problem Statement:
# Each node in the tree can be one of three types:
# - "Leaf": if the node is a leaf node.
# - "Root": if the node is the root of the tree.
# - "Inner": if the node is neither a leaf node nor a root node.
# Write a function to report the type of each node in the tree.
# Return the result table in any order.

# Solution

import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # I create a new column 'type' by applying a lambda function row-wise
    tree['type'] = tree.apply(
        lambda row: 'Root' if pd.isna(row['p_id']) 
                    else 'Inner' if row['id'] in tree['p_id'].values 
                    else 'Leaf',
        axis=1
    )
    
    # I return the result containing 'id' and 'type' columns
    return tree[['id', 'type']]

# Intuition:
# I need to classify each node based on its relationship in the tree:
# - A node with no parent (p_id is null) is a Root.
# - A node that appears as a parent to another node is an Inner node.
# - A node that has a parent but isn't a parent itself is a Leaf.

# Explanation:
# I use `apply` with a lambda function to evaluate each row:
# - If `p_id` is null, the node is classified as 'Root'.
# - If the node's `id` appears in the list of parent IDs (`tree['p_id'].values`), it's an 'Inner' node.
# - Otherwise, the node is a 'Leaf'.
# I then select and return the 'id' and 'type' columns as the final result.
