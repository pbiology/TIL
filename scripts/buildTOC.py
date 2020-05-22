#!/usr/bin/env python

"""
A script to generate a Table Of Content from the folders 
and any markdown files within these folders.
"""

#Import libraries
import os

#Set the path
basepath='/Users/anli/code/TIL'

#folders to exclude
skipfold = {"scripts"}

#Find all relevant folders
folders = []
for entry in os.scandir(basepath):
    if entry.is_dir():
        if entry.name.startswith('.'):
            continue
        if entry.name in skipfold:
            continue
        folders.append(entry.name)

print("Folders to include")
for f in folders:
    print(f)

#Find all 

"""
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
"""
