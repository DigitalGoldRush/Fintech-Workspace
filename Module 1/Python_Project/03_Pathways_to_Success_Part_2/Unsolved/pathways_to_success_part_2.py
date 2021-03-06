"""Pathways to Success Part 2."""
# @TODO: Import the csv library
# YOUR CODE HERE!
import csv
from pathlib import Path

# @TODO: Create a path to the csv file called `quarterly_data.csv`
# YOUR CODE HERE!
csvpath = Path("quarterly_data.csv")

counter = 0 
# @TODO: Open the csv path, read the data, and print each row
with open(csvpath) as (csvfile):
    data = csv.reader(csvfile)
    for row in data:
        counter= counter + 1
        print("row counter ", counter)
        print(row)

"""Extension.

This is an optional extension to the activity.

Create a variable above the `for` loop named `Counter`
and set it equal to zero. Then, every time a new row
is read within the `for` loop, add a value of 1 to
this variable.
"""

# @TODO: Add a row counter to the CSV data.
# YOUR CODE HERE!
