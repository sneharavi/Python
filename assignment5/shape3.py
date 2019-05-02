#!/usr/bin/env python3

from shape2 import *
from math import pi

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
      return "length = %0.2f : width = %0.2f : height = %0.2f" % (self.length, self.width,self.height)


class Cube(Square):
   def __init__(self, length=0):
      Square.__init__(self, length)
   def area(self):
      return 6 * Square.area(self)
   def volume(self):
      return Square.area(self)*self.length
   def __iadd__(self, other):
      return Cube(self.length+other.length)

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

class Cone(Circle):
   def __init__(self, radius=0, height=0):
      Circle.__init__(self, radius)
      self.height = height
   def area(self):
      return Circle.area(self) + 0.5*Circle.perimeter(self)*((self.radius**2)+(self.height**2))**(0.5)
   def volume(self):
      return Circle.area(self)*self.height*(1/3)
   def __iadd__(self, other):
      return Cone(self.radius + other.radius, self.height+other.height)
   def __str__(self):
      return "radius = %0.2f : height = %0.2f" % (self.radius, self.height)

class Sphere(Circle):
   def __init__(self, radius=0):
      Circle.__init__(self, radius)
   def area(self):
      return 4*Circle.area(self)
   def volume(self):
      return (4/3) * Circle.area(self) * self.radius
   def __iadd__(self, other):
      return Sphere(self.radius + other.radius)

class Tetrahedron(equTriangle):
   def __init__(self, a=0):
      equTriangle.__init__(self, a)
   def area(self):
      return 4*equTriangle.area(self)
   def volume(self):
      return (1/3) * equTriangle.area(self) * ((2/3)**0.5)*self.a
   def __iadd__(self, other):
      return Tetrahedron(self.a + other.a)
