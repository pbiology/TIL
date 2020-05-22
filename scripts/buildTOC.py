#!/usr/bin/env python

"""
A script to generate a Table Of Content from the folders 
and any markdown files within these folders.
"""

# Import libraries
import os
import click

# Get arguments from the commandline
@click.command()
@click.option('--tempalte', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')

# Set the path
basepath = '/Users/anli/code/TIL'

# folders to exclude
skipfold = {"scripts"}

# Find all relevant folders
folders = []
for entry in os.scandir(basepath):
    if entry.is_dir():
        if entry.name.startswith('.'):
            continue
        if entry.name in skipfold:
            continue
        folders.append(entry.name)

for folder in sorted(folders):
    print(folder)
print("---")
# Find all markdown in all folders
foldstruct = {}

for folder in sorted(folders):
    print(folder)
    for file in os.scandir(folder):
        if file.is_file() and file.name.endswith('.md'):
            foldstruct[folder] = file
            print(file.name)

for folder, file in foldstruct.items():
    with open(file.path, "r") as md:
        heads = []
        for line in md:
            if line.startswith("### "):
                print(line)
            if line.startswith("##### "):
                print(line)

# Open a file and read stuff
# with open("/Users/anli/code/TIL/conda/condacheat.md","r") as file:
#     id = []
#     for ln in file:
#         if ln.startswith("####"):
#             nohead = ln[5:]
#             id.append(nohead[:-1])
# print(id)

"""
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
"""
