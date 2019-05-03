#!/usr/bin/env python3
"""
CSCI 503 - Assignment 5 - Spring 2019

Author: Sneha Ravi Chandran
Z-ID: z1856678
Date Due: May 02, 2019

Purpose: This API implements various 2D objects
and provides for means  to determine their area,
perimeter and by extension allow for changes.
"""
from math import pi
from shape import Shape

"""
   Class Name:
      class Rectangle(Shape)

   Description:
      A class representing the geometric shape Rectangle
      and inheriting from the abstract classs Shape. The
      class contains the attributes length and width, with
      functions to determine, perimeter and area.
"""
class Rectangle(Shape):
   """
   Function Name:
      __init__()

   Description:
      Constructor for Rectangle class that takes the length and
      width of the side of the Rectangle for the argument.
   Parameters:
      length - length of the Rectangle
      width - width of the Rectangle

   Returns:
      None
   """
   def __init__(self, length=0, width=0):
      # Save length and width of the rectangle.
      self.length = length
      self.width = width
   """
   Function Name:
      perimeter()

   Description:
      class function to calculate and return the perimeter of
      the Rectangle whose length and width exists in the given instance.
   
   Parameters:
      None.

   Returns:
      Returns the perimeter of the Rectangle given
      by the formula P=2*(l+w), where l and w are length and
      width of the rectangle.
   """
   def perimeter(self):
      # return perimeter of rectangle given by P=2*(l+w)
      return 2 * (self.length + self.width)
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the area of
      the Rectangle whose length and width exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of area of the Rectangle calculated
      using the formula A = l*w,  where l and w are length and
      width of the rectangle.
   """
   def area(self):
      # Returns area given by product of lendth and width.
      return self.length * self.width
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Rectangle
      with the length  and width of current instance and the 
      argument added together.
   Parameters:
      other - instance of the class Rectangle to be added
      together.

   Returns:
      Returns an instance of the class Rectangle with the length
      of side of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
       # Return an instance of the rectangle with the dimensions added together.
      return Rectangle(self.length + other.length, self.width + other.width)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the length and width of the Rectangle's
      instance for which it exists.
   """
   def __str__(self):
      # return a formatted string with the length and width up to two decimal digits.
      return "length = %0.2f : width = %0.2f" % (self.length, self.width)

"""
   Class Name:
      class Circle(Shape)

   Description:
      A class representing the geometric shape Circle
      and inheriting from the abstract classs Shape. The
      class contains the attribute radius, with
      functions to determine, perimeter and area.
"""
class Circle(Shape):
   """
   Function Name:
      __init__()

   Description:
      Constructor for Circle that takes the radius of the
      circle as the argument for the instance.
   Parameters:
      radius - radius of the Circle

   Returns:
      None
   """
   def __init__(self, radius=0):
      # intialize and save radius of circle
      self.radius = radius
   """
   Function Name:
      perimeter()

   Description:
      class function to calculate and return the perimeter of
      the Circle whose radius exists in the given instance.
   
   Parameters:
      None.

   Returns:
      Returns the perimeter or circumference of the circle given
      by the formula P=2*pi*r, where r is the radius.
   """
   def perimeter(self):
      # circumference of the circle is given as 2*pi*r
      return float(2 * pi * self.radius)
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the area of
      the Circle whose radius exists in the given instance.
   
   Parameters:
      None.

   Returns:
      Returns the value of area of the Circle calculated
      using the formula A = pi * r * r, where r is the radius
      of the circle.
   """
   def area(self):
      # Area of the circle is given as pi*r*r
      return pi * self.radius * self.radius
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Circle
      with the radius of current instance and the 
      argument added together.
   Parameters:
      other - instance of the class Circle to be added
      together.

   Returns:
      Returns an instance of the class Circle with the
      radius of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
      # new instance of Circle whose radius is sum of the instance and the argument.
      return Circle(self.radius + other.radius)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the radius of the Cirlce's
      instance for which it exists.
   """
   def __str__(self):
       # Returns a formatted string with radius of circle upto two decimal digits.
      return "radius = %0.2f" % self.radius

"""
   Class Name:
      class Triangle(Shape)

   Description:
      A class representing the geometric shape Triangle
      and inheriting from the abstract classs Shape. The
      class contains the attribute length of sides, with
      functions to determine, perimeter and area.
"""
class Triangle(Shape):
   """
   Function Name:
      __init__()

   Description:
      Constructor for Triangle that takes the two shorter
      sides of the Triangle as arguments.
   Parameters:
      a - length of first side of the triangle
      b - length of second side of the triangle
      c - length of third side of the triangle

   Returns:
      None
   """
   def __init__(self, a=0, b=0, c=0):
      # Assign the argument to individual sides of the triangle.
      self.a = a
      self.b = b
      self.c = c
   """
   Function Name:
      perimeter()

   Description:
      class function to calculate and return the perimeter of
      the triangle whose sides exist in the given instance.
   
   Parameters:
      None.

   Returns:
      Returns the value of perimeter of the Triangle given by
      the sum of all its sides.
   """
   def perimeter(self):
      # Perimeter of a triangle determined by sum of sides of the triangle.
      return self.a+self.b+self.c
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the area of
      the triangle whose sides exist int the given instance.
   
   Parameters:
      None.

   Returns:
      Returns the value of area of the Triangle calculated
      using the semi-perimeter i.e., (Heron’s formula).
   """
   def area(self):
      # Determine semi-perimeter.
      k = self.perimeter() / 2
      # Return the are calculated using Heron's formula.
      return (k*(k-self.a)*(k-self.b)*(k-self.c))**(0.5)
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Triangle
      with the dimensions of current instance and the 
      argument added together.
   Parameters:
      other - instance of the class Triangle to be added
      together.

   Returns:
      Returns an instance of the class Triangle with the
      dimensions of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
       # Add all the  respective sides together while returning a new instance.
      return Triangle(self.a + other.a, self.b+other.b, self.c +other.c)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the dimensions of the Triangle's
      instance for which it exists.
   """
   def __str__(self):
      # returns a formatted string of the sides upto two decimal digits.
      return "a = %0.2f : b = %0.2f : c = %0.2f" % (self.a, self.b, self.c)

"""
   Class Name:
      class Square(Rectangle)

   Description:
      A class representing the geometric shape Square
      and inheriting from the class Rectangle. The class
      contains the attribute length of side, with
      functions to determine, perimeter and area.
"""
class Square(Rectangle):
   """
   Function Name:
      __init__()

   Description:
      Constructor for Square class that takes the length of
      the side of the square for the argument.
   Parameters:
      length - length of the side of the square

   Returns:
      None
   """
   def __init__(self, length=0):
      # Both the width and the length are of the same value in the square.
      # A square is a Rectangle of equal length of its sides.
      Rectangle.__init__(self, length, length)
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Square
      with the length of current instance and the 
      argument added together.
   Parameters:
      other - instance of the class Square to be added
      together.

   Returns:
      Returns an instance of the class Square with the length
      of side of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
      # Retun instance of square whose side is the sum of the sides of
      # the instance and the argument suppied to the standard operator.
      return Square(self.length+other.length)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the length of the side of the Square's
      instance for which it exists.
   """
   def __str__(self):
      # returns formatted string with length of the side of square upto
      # two decimal digits.
      return "length = %0.2f" % self.length

"""
   Class Name:
      class rightTriangle(Triangle)

   Description:
      A class representing the geometric shape rightTriangle
      and inheriting from the class Triangle. The class
      contains the attribute length of two shorter sides, with
      functions to determine, perimeter and area.
"""
class rightTriangle(Triangle):
   """
   Function Name:
      __init__()

   Description:
      Constructor for rightTriangle that takes the two shorter
      sides of the right angled triangle as arguments.
   Parameters:
      a - length of one shorter side of the right angled triangle
      b - length of other shorter side of the right angled triangle

   Returns:
      None
   """
   def __init__(self, a=0, b=0):
      self.a = a
      self.b = b
      # A one line version of pythogras formula to compute the longest side of a
      # right triangle.
      self.c = ((a**2) + (b**2))**(0.5)
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class rightTriangle
      with the dimensions of current instance and the 
      argument added together.
   Parameters:
      other - instance of the class rightTriangle to be added
      together.

   Returns:
      Returns an instance of the class rightTriangle with the
      dimensions of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
      # new instance of rightTriangle return with the sum of the respective sides
      # as instance to arguments.
      return rightTriangle(self.a+other.a, self.b+other.b)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the dimensions of the rightTriangle's
      instance for which it exists.
   """
   def __str__(self):
      # returns formatted string with length and height of the right angled triangle
      # upto two decimal places.
      return "length = %0.2f : height = %0.2f" % (self.a, self.b)

"""
   Class Name:
      class equTriangle(Triangle)

   Description:
      A class representing the geometric shape equTriangle
      and inheriting from the class Triangle. The class
      contains the attribute length of the side, with
      functions to determine, perimeter and area.
"""
class equTriangle(Triangle):
   """
   Function Name:
      __init__()

   Description:
      Constructor for equilateral triangle that takes the
      side of the equilateral triangle as an argument.
   Parameters:
      a - length of side of the equilateral triangle

   Returns:
      None
   """
   def __init__(self, a=0):
      # In equilateral triangle all the three sides are equal.
      Triangle.__init__(self, a, a, a)
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class equTriangle
      with the dimensions of current instance and the 
      argument added together.
   Parameters:
      other - instance of the class equTriangle to be added
      together.

   Returns:
      Returns an instance of the class equTriangle with the
      dimensions of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
      # New instance of equilateral triangle whose dimension is the sum of
      # instance and the argument.
      return equTriangle(self.a + other.a)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the dimensions of the equTriangle's
      instance for which it exists.
   """
   def __str__(self):
      # string containing length of side of equilateral triangle returned
      # for upto two decimal digits.
      return "length = %0.2f" % (self.a)
