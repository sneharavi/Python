#!/usr/bin/python3
"""
CSCI 503 - Assignment 2 - Spring 2019

Author: Sneha Ravi Chandran
Z-ID: z1856678
Date Due: February 28, 2019

Purpose: This program takes two file names as arguments and
reads the information from 1st file compute a dictionary of
word frequency and write them to the the second file provided.
"""

import sys
import os
import re

"""
Function Name:
    checkArgs()

Description:
    Reads the arguments from stdin and verifies if the options povided are valid.
    If the paths are valid it returns a tuple of path if not, it exits after printing
    usage.
Parameters:
    None.

Returns:
float: Returns a tuple of both the input file and output file.
"""
def checkArgs():
    invalidUsage = False
    # check if the number of arguments is 3
    if len(sys.argv) != 3:
        invalidUsage = True
    else:
        # verify if the file exists or if the given path is a file
        if not os.path.isfile(sys.argv[1]):
            invalidUsage = True
        elif (sys.argv[1].strip() == '') or (sys.argv[2].strip() == ''):
            invalidUsage = True
    # if the arguments failed the test. print error message and exit execution
    if invalidUsage:
        sys.stderr.write("Usage: %s inFile outFile\n\n" % sys.argv[0])
        sys.exit(1)
    return (sys.argv[1], sys.argv[2])

"""
Function Name:
    openFiles(files)

Description:
    Takes a tuple of files and opens the first file in read mode and opens the
    second file in write mode and return a tuple of fileObjects.
Parameters:
    files -  tuple of file paths to open.

Returns:
    Returns a tuple of file objects on success and on any failure prints error
    messgae and exits.
"""
def openFiles(files):
    inputFile = None
    outputFile = None
    # Check if the file to read exists
    if not os.path.isfile(files[0]):
        # Error out if it doesn't exist
        sys.stderr.write("Can't Open File: %s\n\n" % files[0])
        exit(1)
    # Try to open it in read mode, and handle IOError due to memory or due to file permissions.
    try:
        inputFile = open(files[0], "r")
    except IOError:
        sys.stderr.write("Can't Open File: %s\n\n" % files[0])
        exit(1)
    # Try to open it in write mode, and handle IOError due to memory or due to file permissions.
    try:
        outputFile = open(files[1], "w")
    except IOError:
        sys.stderr.write("Can't Open File: %s\n\n" % files[1])
        exit(1)
    # return a tuple of file objects
    return (inputFile, outputFile)

"""
Function Name:
    closeFiles(fobjects)

Description:
    Takes a list of fileObject and  closes all the files.
    
Parameters:
    fobjects - takes a tuple of file objects and closes all files.

Returns:
    Returns None on success and on any failure prints error messgae and exits.
"""
def closeFiles(fobjects):
    for fileObject in fobjects:
        if fileObject is not None:
            try:
                fileObject.close()
            except IOError:
                sys.stderr.write("Can't close the file %s" % fileObject.name)
            finally:
                exit(1)
        else:
            sys.stderr.write("Cannot close file.")
            exit(1)
    return

"""
Function Name:
     createList(inFileObj)

Description:
    Takes a object to file, parses the string into a list of strings by splitting
    on whitespaces and dashes and returns it.
    
Parameters:
    inFileObj - Object of file to parse into word list.

Returns:
    Returns a populated list on successfully reading and parsing the file.
"""
def createList(inFileObj):
    listOfWords = list()
    # Compile a regex to look for whitespaces and dashes to split the lines into a list.
    regexToSplitLine = re.compile(r'[\s-]+', re.MULTILINE | re.IGNORECASE | re.VERBOSE)
    try:
        # Read from file object by line.
        for line in inFileObj:
            # split the line based on regex (empty words will be included)
            for word in regexToSplitLine.split(line.strip()):
                listOfWords.append(word.strip())
    except IOError:
        return list()
    return listOfWords

"""
Function Name:
    createDictionary(words)

Description:
    Takes a list of words, strips them off of non-alphabetic characters and populates
    a  dictionary of words and their count.
    
Parameters:
    words - list of words to parse into dictionary.

Returns:
    Returns a populated dictionary of words and their frequency.
"""
def createDictionary(words):
    alphabeticWords = list()
    freqDictionary = dict()
    regexString = '^[^A-Z0-9]+|[^A-Z0-9]+$'
    regexToSplitWord = re.compile(r'[\W0-9]', re.MULTILINE | re.IGNORECASE | re.VERBOSE)
    for word in words:
        alphabeticWord = re.sub(regexString, '', word, flags=re.IGNORECASE | re.MULTILINE).strip()
        if alphabeticWord:
            cleanedWord = regexToSplitWord.split(alphabeticWord)[0].strip().lower()
            if cleanedWord:
                alphabeticWords.append(cleanedWord)
    for items in alphabeticWords:
        freqDictionary[items] = alphabeticWords.count(items)
    return {word:alphabeticWords.count(word) for word in sorted(freqDictionary.keys())}

"""
Function Name:
    printDictionary()

Description:
    Generates a dictionary of words and their frequency by reading a file and saves
    it to another file provided as part of command line argument.
    
Parameters:
    None.

Returns:
    Returns None.
"""
def printDictionary():
    """printDictionary() computes frequency Dictionary from the given file."""
    filesToScan = checkArgs()
    frequencyDictionary = dict()
    openFileObjects = openFiles(filesToScan)
    writeFileObject = openFileObjects[1]
    words = createList(openFileObjects[0])
    frequencyDictionary = createDictionary(words)
    column = 1
    try:
        writeFileObject.write("Output Values for Data: {0:s}\n".format(os.path.abspath(filesToScan[0])))
        writeFileObject.write("---------------------------------------------------------\n")
        writeFileObject.write("size = {0:d}\n\n".format(len(frequencyDictionary)))
        for word in frequencyDictionary:
            writeFileObject.write("{0:16s}:{1:3d}\t".format(word, frequencyDictionary[word]))
            if column % 3 == 0:
                writeFileObject.write("\n")
                column = 1
            else:
                column += 1
                if word == list(frequencyDictionary.keys())[-1]:
                    writeFileObject.write("\n")
         # Write new line at end of file.
        if frequencyDictionary:
            writeFileObject.write("\n")
        closeFiles(openFileObjects)
    except IOError:
        sys.stderr.write("Failed to write word-frequency dictionary to file: "+ writeFileObject.name)
    return

def main():
    """Main function"""
    printDictionary()

if __name__ == '__main__':
    main()
