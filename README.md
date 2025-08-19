# genderquickchecker_PL
Python code to quick gender check of polish employees.

Gender Detection Script for Excel Data
This Python script reads an Excel file containing a list of names (in the first column), determines the likely gender based on simple rules, and writes the result to a new column called gender.

Features
Reads names from the first column of an Excel file.
Applies basic logic to guess gender:
Names ending with "a" are assumed to be female ("K").
All other names are assumed to be male ("M").
Specific exceptions like "Kuba", "Barnaba", and "Dyzma" are treated as male regardless of the ending.
Adds a new column "gender" with the result.
Saves the updated file, overwriting the original.
