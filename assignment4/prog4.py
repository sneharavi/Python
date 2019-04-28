#!/usr/bin/python3

import sys
from rational import Rational

# rational test: A test driver for rational.py module.

def main ():
   generalTests()
   errorTests()

def generalTests():
   """Test basic functionality.
      Test constructor."""

   """Test read () method."""

   R = Rational.read ();
   i = 1
   while R:
      print('R', i, ' = ', R, sep = '', end = ' ')
      if type(R) != str: print( '(', float(R), ')') 
      R = Rational.read (); 
      i += 1
   print()

def errorTests ():
   """Test error conditions."""

   try:
      r5 = Rational(5, 0)
   except ZeroDivisionError:
      sys.stderr.write ( "Error: invalid rational number: 5/0\n")

if __name__ == "__main__": main ()
