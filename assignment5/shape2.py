#!/usr/bin/env python3

from shape import Shape
from math import pi

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

class Triangle(Shape):
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   def perimeter(self):
      return self.a+self.b+self.c
   def area(self):
      k = self.perimeter() / 2
      return (k*(k-self.a)*(k-self.b)*(k-self.c))**(0.5)
   def __iadd__(self, other):
      return Triangle(self.a + other.a, self.b+other.b, self.c +other.c)
   def __str__(self):
      return "a = %0.2f : b = %0.2f : c = %0.2f" % (self.a, self.b, self.c)

class Square(Rectangle):
   def __init__(self, side):
      self.length = side
      self.width = side
   def __iadd__(self, other):
      return Square(self.width+other.width)
   def __str__(self):
      return "length = %0.2f" % self.length

class rightTriangle(Triangle):
   def __init__(self, a, b):
      Triangle.__init__(self, a, b, ((a**2) + (b**2))**(0.5))
   def __iadd__(self, other):
      return rightTriangle(self.a+other.a, self.b+other.b)
   def __str__(self):
      return "length = %0.2f : height = %0.2f" % (self.a, self.b)

class equTriangle(Triangle):
   def __init__(self, a):
      Triangle.__init__(self, a, a, a)
   def __str__(self):
      return "length = %0.2f" % (self.a)
   def __iadd__(self, other):
      return equTriangle(self.a + other.a)
      
