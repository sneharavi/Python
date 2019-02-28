#!/usr/bin/python3
"""
CSCI 503 - Assignment 1 - Spring 2019

Author: Sneha Ravi Chandran
Z-ID: z1856678
Date Due: February 7, 2019

Purpose: This program accepts  a series of numbers from stdin, calculates
and prints various statistical information including Lowest Number of the 
input, Higher Number, Mean and Standard Deviation.
"""
import sys
from math import sqrt

"""
Function Name:
    read_data (numbers)
        
Description: 
    Reads from stdin and saves it to the reference of  list passed to
    it as an argument.
Parameters: 
    numbers - List to save the elements red from stdin.

Returns: 
float: Returns None
"""

def read_data (numbers):
    # Take all lines from stdin
    lines_from_file = sys.stdin.readlines()
    for number_at_line in lines_from_file:
        # read lines to a list
        numbers.append(float(number_at_line.rstrip()))
    # return control to the caller.
    return None

"""
Function Name:
    std_deviation(numbers , mean)
        
Description: 
    Calculates standard deviation for given list of numbers and their mean.

Parameters: 
    numbers - List of all the number whose standard deviation is to be determined.
    mean    - Mean of the list of numbers.
Returns: 
    float: Returns the calculated standard deviation of the list of numbers.
"""

def std_deviation (numbers, mean):
    # Cannot calculate standard deviation if number of elements is 1
    if(len(numbers) <= 1):
        # if number of element is 1, there is no standard deviation.
        return 0
    # Initialize the value to calculate squarred value of (element - mean)
    squarred_sum = 0
    for number in numbers:
        squarred_sum += (number - mean)**2
    # calculate and return standard deviation.
    return sqrt(float(squarred_sum/(len(numbers)-1)))

"""
Function Name:
    print_stat ()

Description: 
    Prints statistics data of Lowest Number, Highest Number, Mean, Standard
    Deviation of input data from input given through stdin.

Parameters: 
    None.

Returns: 
    None
"""

def print_stat ():
    # Initialize a list
    numbers = list()
    
    # Initialize intial values of all variables to be used in calculation.
    mean = ""
    standard_deviation = ""
    minimum_number = ""
    maximum_number = ""
    
    # Read data from stdin and save it 
    read_data(numbers)
    
    # calculate and print all statistics data
    print("Output Statistics for Input Data")
    print("--------------------------------")
    if len(numbers) > 0:
        # All numbers are saved and formated into string with 10 integer spaces and two decimal spaces.
        # Mean rounded off to two digits is Sum of numbers in list divided by number of elements
        mean = "%10.2f" % (round(sum(numbers)/len(numbers),2))
        # SD is square root of sum of squares after dividing by N-1 where N is number of elements
        standard_deviation = "%10.2f" % (round(std_deviation(numbers, float(mean)),2))
        # Smallest number in the list
        minimum_number = "%10.2f" % (round(min(numbers),2))
        # Largest number in the list
        maximum_number = "%10.2f" % (round(max(numbers),2))
    
    # Print all data with numbers to be right aligned.
    print("Low:    %s" % minimum_number)
    print("High:   %s" % maximum_number)
    print("Mean:   %s" % mean)
    print("StdDev: %s" % standard_deviation)
    return None

# main function defentition.
def main ():
    """ Main function """
    # print statistics data
    print_stat()

if __name__ == '__main__':
    main()
