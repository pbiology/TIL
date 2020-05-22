#!/usr/bin/env python

"""
A script to generate a Table Of Content from the folders 
and any markdown files within these folders.
"""

# Import libraries
import os
import click

def readTemplate(template):
    with open(template, "r") as templateFile:
        start_text = templateFile.read()
        return start_text

def exclude_list(exclude):
    try:
        return exclude.split(',')
    except AttributeError:
        return []

# Get arguments from the commandline
@click.command()
@click.option('-t', '--template', required=True, help='Path to template file')
@click.option('-s', '--start', required=True, help='Starting directory')
@click.option('-e','--exclude', help='Comma-separated list of directories to exclude')
def main(start, template, exclude):
    # Print start of file
    print(readTemplate(template).rstrip())

    # folders to exclude
    skipfold = exclude_list(exclude)

    # Find all relevant folders
    folders = []
    for entry in os.scandir(start):
        if entry.is_dir():
            if entry.name.startswith('.'):
                continue
            if entry.name in skipfold:
                continue
            folders.append(entry.name)
    #Print folder names as top level TOC (Categories)
    print('### Categories\n')
    for folder in sorted(folders):
        print('* [{0}](#{1})'.format(folder.capitalize(), folder))
    print("\n---")

    # Find all markdown in all folders and print
    # Store them in a dictionary
    foldstruct = {}

    for folder in sorted(folders):
        for file in os.scandir(folder):
            if file.is_file() and file.name.endswith('.md'):
                if folder in foldstruct:
                    foldstruct[folder].append(file)
                else:
                    foldstruct[folder] = [file]

    for folder, file_list in foldstruct.items():
        print('### {0}'.format(folder.capitalize()))
        for file in file_list:
            print ("> {0}\n".format(file.name))
            with open(file.path, "r") as md:
                for line in md:
                    if line.startswith("### "):
                        print("\n##### [{0}]({1}/{2}#{3})".format(line[4:].rstrip(), folder,
                            file.name, line[4:].rstrip().replace(" ","-")))
                    if line.startswith("##### "):
                        print("* [{0}]({1}/{2}#{3})".format(line[6:].rstrip(), folder,
                            file.name, line[6:].rstrip().replace(" ", "-")))
                        #print(" * [{0}]({1}#{2})".format(line[6:].rstrip(), folder,
                        #line[6:].rstrip().replace(" ","-")))
                        #print(" * {0}".format(line[6:].rstrip()))
        print("\n---")

if __name__ == '__main__':
    main()
