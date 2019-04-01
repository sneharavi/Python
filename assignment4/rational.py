#!/usr/bin/env python3
"""
CSCI 503 - Assignment 4 - Spring 2019

Author: Sneha Ravi Chandran
Z-ID: z1856678
Date Due: April 16, 2019

Purpose: This implementation of Rational can be used to parse 
and save Rational Numbers as an object by assignment or by 
reading from stdin. The implementation also allowes to perform
basic arithmatic computations and logical computations between
two rational number objects using operator overloading.
"""
import sys

"""
   Class Name:
      class Raiona(num,den)
   
   Description:
      Create a new Rational object from the given numerator and
      denominator integer values supplied as arguments. Any
      non-numerical as argument or stdin prints error message to
      stderr but doesn't affect the exexcution of the code. class
      overloads many basic artihmatic and logical operaions along
      with overriding read() function to read the from stdin.

"""
class Rational:
   """
   Function Name:
      __init__()

   Description:
      Constructor to parse and save numerator and denominator components of the
      rational number. The constructor prints error message to stderr if the
      denominator is 0.
   Parameters:
      num - numerator of the instance to be created.
      den - denominator of the instance to be created, default value being 1.

   Returns:
      None
   """
   def __init__(self, num=0, den=1):
      if den == 0:
         # Print error if denominator is zero
         print('Error: invalid rational number: {}/{}'.format(num, den), file=sys.stderr)
         # Save data and continue exexcution.
         self.den = 0
         self.num = num
      else:
         # Obtain GCD of the numberator and denominator.
         gcdOfFraction = gcd(num, den)
         # Dividing by GCD gives the least values of both of them.
         self.num = int(num / gcdOfFraction)
         self.den = int(den / gcdOfFraction)
   """
   Function Name:
      __add__()

   Description:
      Function overloads '+' operator and returns the computed sum of 
      its arguments.
   Parameters:
      other - an instance of Rational class which would be the added to get the
      instance , giving the sum of them.
   Returns:
      Returns objects of class type rational whose is a sum of instance and argument.
   """
   def __add__(self, other):
      # Compute sum of numerator equivaluents.
      sumOfNum = self.num * other.den + other.num * self.den
      # Get equivalent denominator result needed of the sum of fractions.
      productOfDen = self.den * other.den
      # Returns insance with reduced rational equivalence.
      return Rational(sumOfNum, productOfDen)
   """
   Function Name:
      __sub__()

   Description:
      Function overloads '-' operator and returns the computed difference of 
      its arguments.
   Parameters:
      other - an instance of Rational class which would be the subtrahend with
      the minuend being instance itself.
   Returns:
      Returns objects of class type rational whose is a difference of instance and argument.
   """
   def __sub__(self, other):
      # Compute difference of numerator equivaluents.
      diffOfNum = self.num * other.den - self.den * other.num
      # Get equivalent denominator result needed of the sum of fractions.
      productOfDen = self.den * other.den
      # Returns insance with reduced rational equivalence.
      return Rational(diffOfNum, productOfDen)
   """
   Function Name:
      __mul__()

   Description:
      Function overloads '*' operator and returns the computed product of 
      its arguments.
   Parameters:
      other - an instance of Rational class which would be the product with
      the insance itself.
   Returns:
      Returns objects of class type rational whose is a product of instance and argument.
   """
   def __mul__(self, other):
      # Get separate Products of numerato and denominator
      # Returns insance with reduced rational equivalence.
      return Rational(self.num * other.num, other.den * self.den)
   """
   Function Name:
      __truediv__()

   Description:
      Function overloads '/' operator and returns the computed quotient by
      dividing the instance with argument.
   Parameters:
      other - an instance of Rational class which would be the dividend of
      the insance itself.
   Returns:
      Returns objects of class type rational whose is a division of instance and argument.
   """
   def __truediv__(self, other):
      # Get separate Products of numerator and denominator with argument elements.
      # Returns insance with reduced rational equivalence.
      return Rational(self.num * other.den, self.den * other.num)
   """
   Function Name:
      __neg__()

   Description:
      Function overloads the unary negate operation and gives the negative of the
      instance itself.
   Parameters:
      None
   Returns:
      Returns the negated value of the instance.
   """
   def __neg__(self):
      # Returns insance with reduced rational  negative equivalence .
      return Rational(-1*self.num, self.den)
   """
   Function Name:
      __eq__()

   Description:
      Function overloads equality logical operator and compares the instance with
      the argument supplied to it.
   Parameters:
      other - an instance of Rational class which is to be compared to the argument
      for equality with the instace object.
   Returns:
      Returns True if the entities are equal.
   """
   def __eq__( self, other ):
      # Return True if both objects are of equal.
      return self.num == other.num and self.den == other.den
   """
   Function Name:
      __ne__()

   Description:
      Function overloads not equal (!=) logical operator and compares the instance with
      the argument supplied to it.
   Parameters:
      other - an instance of Rational class which is to be compared to the argument
      for inequality with the instace object.
   Returns:
      Returns True if the entities are unequal.
   """
   def __ne__( self, other ):
      # Return True if both objects are of not equal.
      return self.num != other.num or self.den != other.den
   """
   Function Name:
      __lt__()

   Description:
      Function overloads "<" logical operator and compares the instance with
      the argument supplied to it.
   Parameters:
      other - an instance of Rational class which is to be compared to the 
      argument with the instace object.
   Returns:
      Returns  True if the instance is less than the argument.
   """
   def __lt__( self, other ):
      #  if denominators are equal compare numerators alone to get status.
      if self.den == other.den:
         if self.num < other.num:
            return True
      else:
         # Check if the LCM equalivalent values are lesser than argument given.
         commonMultiple = (self.den *  other.den) / gcd(self.den, other.den)
         if self.num * commonMultiple/self.den < other.num * commonMultiple/other.den:
            return True
      return False
   """
   Function Name:
      __gt__()

   Description:
      Function overloads ">" logical operator and compares the instance with
      the argument supplied to it.
   Parameters:
      other - an instance of Rational class which is to be compared to the
      argument with the instace object.
   Returns:
      Returns  True if the instance is greater than the argument.
   """
   def __gt__ ( self, other ):
      #  if denominators are equal compare numerators alone to get status.
      if self.den == other.den:
         if self.num > other.num:
            return True
      else:
         # Check if the LCM equalivalent values are greater than argument given.
         commonMultiple = (self.den *  other.den) / gcd(self.den, other.den)
         if self.num * commonMultiple/self.den > other.num * commonMultiple/other.den:
            return True
      return False
   """
   Function Name:
      __le__()

   Description:
      Function overloads "<=" logical operator and compares the instance with
      the argument supplied to it.
   Parameters:
      other - an instance of Rational class which is to be compared to the
      argument with the instace object.
   Returns:
      Returns  True if the instance is lesser than or equal to the argument.
   """
   def __le__( self, other ):
      #  check if number if greater than the argument.
      if self.__gt__(other):
         return False
      # Check if they are equal.
      if self.__eq__(other):
         return True
      # check if its less than argument.
      if self.__lt__(other):
         return True
      return False
   """
   Function Name:
      __ge__()

   Description:
      Function overloads ">=" logical operator and compares the instance with
      the argument supplied to it.
   Parameters:
      other - an instance of Rational class which is to be compared to the
      argument with the instace object.
   Returns:
      Returns  True if the instance is greater than or equal to the argument.
   """
   def __ge__(self, other):
      #  check if number if less than the argument.
      if self.__lt__(other):
         return False
      # Check if they are equal.
      if self.__eq__(other):
         return True
      # check if its greater than argument.
      if self.__gt__(other):
         return True
      return False
   """
   Function Name:
      __str__()

   Description:
      Function provides for a string interpretation of the instance.
   Parameters:
      None.
   Returns:
      Returns string equivaluent of the instance object.
   """
   def __str__( self ):
      # if denominator is 1 , return string of numerator.
      if self.den == 1:
         return str(self.num)
      # return formatted string of the fraction.
      return '{}/{}'.format(self.num, self.den)
   """
   Function Name:
      __float__()

   Description:
      Function returns the float equivaluent of the instance.
   Parameters:
      None.
   Returns:
      Returns the decimal (float) equivaluent of the object instance.
   """
   def __float__(self):
      return float(self.num)/float(self.den)
   """
   Function Name:
      read()

   Description:
      Function read instance to a Rational() instance object.
   Parameters:
      None.
   Returns:
      Returns  a new instance of Raional class from parsed data.
   """
   def read():
      # Strip all whitespace
      inputString = sys.stdin.readline().strip(" \r\n\t")
      # if element is not empty proceed else return a whitespace character.
      if inputString:
         # split string to a list and strip them from whitespace.
         inputNumbers = [str(unprocessedString).strip(" \r\n\t") for \
                         unprocessedString in inputString.split('/')]
         # Try and catch any parsing exceptions.
         try:
            # if its an integer(no denominator part) return its equivalent.
            if len(inputNumbers) == 1:
               return Rational(int(inputNumbers[0]), 1)
            # if the input given is invalid print error and return empty white space.
            if len(inputNumbers) > 2:
               print("Error: invalid rational number:", inputString, file=sys.stderr)
               return " "
            # Return Rational object if the two elements of the list are good.
            return Rational(int(inputNumbers[0]), int(inputNumbers[-1]))
         except Exception:
            # Print error string if exception occurs.
            print("Error: invalid rational number:", inputString, file=sys.stderr)
            return " "
         # return whitespace character ' ' by default.
         return " "
"""
Function Name:
   gcd(num, den)

Description:
   Function gets the greatest common divisor of two numbers.
Parameters:
   num, den - arguments whose G.C.D. needs to be determined.

Returns:
   Returns the G.C.D. of two numbers.
"""
def gcd(num, den):
   # Everything divides 0
   if den == 0:
      return num
   # Recursively compute GCD.
   return gcd(den, num % den)
