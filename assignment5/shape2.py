#!/usr/bin/env python3

from shape import Shape
from math import pi

class Rectangle(Shape):
   def __init_(self, length, width):
      self.length = length
      self.width = width
   def perimeter(self):
      return 2 * (self.length + self.width)
   def area(self):
      return self.length * self.width()

class Circle(Shape):
   def __init_(self, radius):
      self.radius = radius
   def perimeter(self):
      return 2 * pi * self.radius
   def area(self):
      return pi * self.radius * self.radius

class Triangle(Shape):
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   def perimeter(self):
      return self.a+self.b+self.c
   def area(self):
      k = self.perimeter() / 2
      return (k*(k-self.a)*(k-self.b)*(k-self.c))^(0.5)

class Square(Rectangle):
   def __init_(self, side):
      Rectangle.length = side
      Rectangle.width = side
   def perimeter(self):
      return Rectangle.perimeter()
   def area(self):
      return Rectangle.area()

class rightTriangle(Triangle):
   __str__(self):
   
