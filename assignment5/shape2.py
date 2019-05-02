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
   def __init__(self, length=0, width=0):
      self.length = length
      self.width = width
   def perimeter(self):
      return 2 * (self.length + self.width)
   def area(self):
      return self.length * self.width
   def __iadd__(self, other):
      return Rectangle(self.length + other.length, self.width + other.width)
   def __str__(self):
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
   def __init__(self, radius):
      self.radius = radius
   def perimeter(self):
      return float(2 * pi * self.radius)
   def area(self):
      return pi * self.radius * self.radius
   def __iadd__(self, other):
      return Circle(self.radius + other.radius)
   def __str__(self):
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
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   def perimeter(self):
      return self.a+self.b+self.c
   def area(self):
      # Determine semi-perimeter.
      k = self.perimeter() / 2
      return (k*(k-self.a)*(k-self.b)*(k-self.c))**(0.5)
   def __iadd__(self, other):
      return Triangle(self.a + other.a, self.b+other.b, self.c +other.c)
   def __str__(self):
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
   def __init__(self, length):
      self.length = length
      self.width = length
   def __iadd__(self, other):
      return Square(self.length+other.length)
   def __str__(self):
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
   def __init__(self, a, b):
      self.a = a
      self.b = b
      self.c = ((a**2) + (b**2))**(0.5)
   def __iadd__(self, other):
      return rightTriangle(self.a+other.a, self.b+other.b)
   def __str__(self):
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
   def __init__(self, a):
      Triangle.__init__(self, a, a, a)
   def __str__(self):
      return "length = %0.2f" % (self.a)
   def __iadd__(self, other):
      return equTriangle(self.a + other.a)
