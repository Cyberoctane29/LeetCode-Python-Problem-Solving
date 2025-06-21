# Problem 3570: Find Books with No Available Copies
# Difficulty: Easy

# Table: library_books
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | book_id          | int     |
# | title            | varchar |
# | author           | varchar |
# | genre            | varchar |
# | publication_year | int     |
# | total_copies     | int     |
# +------------------+---------+
# book_id is the unique identifier for this table.
# Each row contains information about a book in the library, including the total number of copies owned by the library.

# Table: borrowing_records
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | record_id     | int     |
# | book_id       | int     |
# | borrower_name | varchar |
# | borrow_date   | date    |
# | return_date   | date    |
# +---------------+---------+
# record_id is the unique identifier for this table.
# Each row represents a borrowing transaction and return_date is NULL if the book is currently borrowed and hasn't been returned yet.

# Problem Statement:
# Write a function to find all books that are currently borrowed (not returned) and have zero copies available in the library.
# A book is considered currently borrowed if there exists a borrowing record with a NULL return_date.
# Return the result table ordered by current_borrowers in descending order, then by book title in ascending order.

# Solution

import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    # I count how many current borrowers (records with null return_date) exist for each book_id
    temp_df = borrowing_records.groupby('book_id', as_index=False).apply(
        lambda x: pd.Series({'current_borrowers': x.loc[x['return_date'].isna(), 'record_id'].count()})
    )

    # I merge this borrower count with the library_books table on book_id
    merged_df = pd.merge(library_books, temp_df, how='inner', on='book_id')

    # I compute remaining copies by subtracting current borrowers from total_copies
    merged_df['remaining'] = merged_df['total_copies'] - merged_df['current_borrowers']

    # I filter for books where remaining copies are zero
    result_df = merged_df.loc[merged_df['remaining'] == 0, :]

    # I drop unnecessary columns and sort the result
    result_df = result_df.drop(columns=['total_copies', 'remaining']).sort_values(
        by=['current_borrowers', 'title'], ascending=[False, True]
    )

    # I return the final result
    return result_df

# Intuition:
# I need to find books that have all their copies currently borrowed.
# I first count how many ongoing (not returned) borrowings exist for each book.
# Then, I compare this with the total number of copies the library owns.
# If the number of current borrowers equals the total number of copies, the book is out of stock.
# I return such books along with the number of current borrowers.

# Explanation:
# I use groupby + apply to count how many borrowing_records per book_id have a null return_date.
# I merge this result with the library_books table to get total_copies and other book details.
# Then, I compute the remaining available copies by subtracting current borrowers.
# I filter for rows where remaining copies are zero, meaning no copies are available.
# Finally, I sort the result by current_borrowers in descending order, and by title alphabetically, and drop unneeded columns.