#!/usr/bin/env python3
"""
CSCI 503 - Assignment 5 - Spring 2019

Author: Sneha Ravi Chandran
Z-ID: z1856678
Date Due: May 02, 2019

Purpose: This API implements various 3D objects
and provides for means  to determine their area, 
volume and by extension allow for changes.
"""
from shape2 import *

"""
   Class Name:
      class Box(Rectangle)

   Description:
      A class representing the 3-D geometric shape Box
      and inheriting from the class Rectangle. The class
      contains the attribute length ,width and height, with
      functions to determine, volume and surface area.
"""
class Box(Rectangle):
   def __init__(self, length=0, width=0, height=0):
      self.length = length
      self.width = width
      self.height = height
   def area(self):
      return (2 * Rectangle.area(self)) + (self.height * Rectangle.perimeter(self))
   def volume(self):
      return Rectangle.area(self)*self.height
   def __iadd__(self,other):
      return Box(self.length+other.length, self.width+other.width, self.height+self.height)
   def __str__(self):
      return "length = %0.2f : width = %0.2f : height = %0.2f" % (self.length, self.width, self.height)

"""
   Class Name:
      class Cube(Square)

   Description:
      A class representing the 3-D geometric shape Cube
      and inheriting from the class Square. The class
      contains the attribute length of the side, with
      functions to determine, volume and surface area.
"""
class Cube(Square):
   def __init__(self, length=0):
      Square.__init__(self, length)
   def area(self):
      return 6 * Square.area(self)
   def volume(self):
      return Square.area(self)*self.length
   def __iadd__(self, other):
      return Cube(self.length+other.length)

"""
   Class Name:
      class Cylinder(Circle)

   Description:
      A class representing the 3-D geometric shape Cylinder
      and inheriting from the class Circle. The class
      contains the attribute base radius and height, with
      functions to determine, volume and surface area.
"""
class Cylinder(Circle):
   def __init__(self, radius=0, height=0):
      Circle.__init__(self, radius)
      self.height = height
   def area(self):
      return 2 * Circle.area(self) + 2 *pi * self.radius * self.height
   def volume(self):
      return Circle.area(self)*self.height
   def __iadd__(self, other):
      return Cylinder(self.radius + other.radius, self.height+other.height)
   def __str__(self):
      return "radius = %0.2f : height = %0.2f" % (self.radius, self.height)

"""
   Class Name:
      class Cone(Circle)

   Description:
      A class representing the 3-D geometric shape Cone
      and inheriting from the class Circle. The class
      contains the attribute base radius and height, with
      functions to determine, volume and surface area.
"""
class Cone(Circle):
   def __init__(self, radius=0, height=0):
      self.radius = radius
      self.height = height
   def area(self):
      return Circle.area(self) + 0.5*Circle.perimeter(self)*((self.radius**2)+(self.height**2))**(0.5)
   def volume(self):
      return Circle.area(self)*self.height*(1/3)
   def __iadd__(self, other):
      return Cone(self.radius + other.radius, self.height+other.height)
   def __str__(self):
      return "radius = %0.2f : height = %0.2f" % (self.radius, self.height)

"""
   Class Name:
      class Sphere(Circle)

   Description:
      A class representing the 3-D geometric shape Sphere
      and inheriting from the class Circle. The class
      contains the attribute base radius, with
      functions to determine, volume and surface area.
"""
class Sphere(Circle):
   def __init__(self, radius=0):
      self.radius = radius
   def area(self):
      return 4*Circle.area(self)
   def volume(self):
      return (4/3) * Circle.area(self) * self.radius
   def __iadd__(self, other):
      return Sphere(self.radius + other.radius)

"""
   Class Name:
      class Tetrahedron(equTriangle)

   Description:
      A class representing the 3-D geometric shape Tetrahedron
      and inheriting from the class equTriangle. The class
      contains the attribute side of the Tetrahedron, with
      functions to determine, volume and surface area.
"""
class Tetrahedron(equTriangle):
   def __init__(self, a=0):
      equTriangle.__init__(self, a)
   def area(self):
      return 4*equTriangle.area(self)
   def volume(self):
      return (1/3) * equTriangle.area(self) * ((2/3)**0.5)*self.a
   def __iadd__(self, other):
      return Tetrahedron(self.a + other.a)
