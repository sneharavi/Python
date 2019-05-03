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
   """
   Function Name:
      __init__()

   Description:
      Constructor for Box class inheriting Rectangle class
      takeing length, width and height of the Box for the arguments.
   
   Parameters:
      length - length of the Box
      width - width of the Box
      height - width of the Box

   Returns:
      None
   """
   def __init__(self, length=0, width=0, height=0):
      self.length = length
      self.width = width
      self.height = height
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the surface area of
      the Box whose length,width and height exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of area of the Box calculated using the formula
      𝐴= 2𝐴0 + ℎ𝑃0 where 𝐴0 is the area and 𝑃0 is the perimeter of the
      top of the box
   """
   def area(self):
      return (2 * Rectangle.area(self)) + (self.height * Rectangle.perimeter(self))
   """
   Function Name:
      volume()

   Description:
      class function to calculate and return the volume of
      the Box whose length,width and height exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of volume of the Box calculated using the formula
      𝑉 = ℎ𝐴0 where 𝐴0 is the area of the top of the box.
   """
   def volume(self):
      return Rectangle.area(self)*self.height
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Box with the
      length, width  and height of current instance and the 
      argument added together.
   
   Parameters:
      other - instance of the class Box to be added
      together.

   Returns:
      Returns an instance of the class Box with dimensions
      of both the intstance itself and the argument supplied
      added together.
   """
   def __iadd__(self,other):
      return Box(self.length+other.length, self.width+other.width, self.height+self.height)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   Parameters:
      None.

   Returns:
      Returns a string containing the length width and height of the Box's
      instance for which it exists up to two decimal digits.
   """
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
   """
   Function Name:
      __init__()

   Description:
      Constructor for Cube class inheriting Square class
      takeing length of side of the Cube for the arguments.
   
   Parameters:
      length - length of the Cube

   Returns:
      None
   """
   def __init__(self, length=0):
      Square.__init__(self, length)
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the surface area of
      the Cube whose length of the side exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of area of the Cube calculated using the formula
      𝐴= 6𝐴0  where 𝐴0 is the area of one face of the Cube
   """
   def area(self):
      # A cuble has 6 square faces and hence the surface area is 6*A0.
      return 6 * Square.area(self)
   """
   Function Name:
      volume()
   
   Description:
      class function to calculate and return the volume of
      the Cube whose length of side exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of volume of the Cube calculated using the formula
      𝑉 = ℎ𝐴0 where 𝐴0 is the area of the top of the cube's face.
   """
   def volume(self):
      return Square.area(self)*self.length
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Cube with the
      length of side of cube of current instance and the 
      argument added together.
   
   Parameters:
      other - instance of the class Cube to be added
      together.

   Returns:
      Returns an instance of the class Cube with the length
      of side of both the intstance itself and the argument
      supplied added together.
   """
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
   """
   Function Name:
      __init__()

   Description:
      Constructor for Cylinder class inheriting Circle class
      takeing radius and height of the Cylinder for the arguments.
   
   Parameters:
      radius - radius of the Cylinder
      height - length of the Cylinder
   
   Returns:
      None
   """
   def __init__(self, radius=0, height=0):
      Circle.__init__(self, radius)
      # new attribute for Cylinder
      self.height = height
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the surface area of
      the Cylinder whose radius and height exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of surface area of the cylinder calculated using the formula
      A = 2𝐴0 + 𝐴1 where 𝐴0 is the area of the base and 𝐴1 is the area of the
      lateral surface of the cylinder. r. If 𝑃0 is the perimeter
      of the base of the cylinder, then 𝐴1 = ℎ𝑃0.
   """
   def area(self):
      return 2 * Circle.area(self) + Circle.perimeter(self)  * self.height
   """
   Function Name:
      volume()
   
   Description:
      class function to calculate and return the volume of
      the cylinder whose radius and height exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of volume of the Cylinder calculated using the formula
      𝑉 = ℎ𝐴0 where 𝐴0 is the area of the base of  Cylinder.
   """
   def volume(self):
      return Circle.area(self)*self.height
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Cylinder with the
      radius and height of current instance and the 
      argument added together.
   
   Parameters:
      other - instance of the class Cylinder to be added
      together.

   Returns:
      Returns an instance of the class Cylinder with dimensions
      of both the intstance itself and the argument supplied
      added together.
   """
   def __iadd__(self, other):
      return Cylinder(self.radius + other.radius, self.height+other.height)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   
   Parameters:
      None.

   Returns:
      Returns a string containing the radius and height of the Cylinder's
      instance for which it exists up to two decimal digits.
   """
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
   """
   Function Name:
      __init__()

   Description:
      Constructor for Cone class inheriting Circle class
      takeing radius and height of the Cone for the arguments.
   
   Parameters:
      radius - radius of the Cone
      height - length of the Cone
   
   Returns:
      None
   """
   def __init__(self, radius=0, height=0):
      self.radius = radius
      self.height = height
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the surface area of
      the Cone whose radius and height exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of surface area of the Cone calculated using the formula
      A = 𝐴0 + 𝐴1 where 𝐴0 is the area of the base and and 𝐴𝐴1 is the area of the
      lateral surface of the cone.
   """
   def area(self):
      return Circle.area(self) + 0.5*Circle.perimeter(self)*((self.radius**2)+(self.height**2))**(0.5)
   """
   Function Name:
      volume()
   
   Description:
      class function to calculate and return the volume of
      the cylinder whose radius and height exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of volume of the Cylinder calculated using the formula
      𝑉 = (1/3)ℎ𝐴0 where 𝐴0 is the area of the base of  Cylinder.
   """
   def volume(self):
      return (1/3)*Circle.area(self)*self.height
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Cone with the
      radius and height of current instance and the 
      argument added together.
   
   Parameters:
      other - instance of the class Cone to be added
      together.

   Returns:
      Returns an instance of the class Cone with dimensions
      of both the intstance itself and the argument supplied
      added together.
   """
   def __iadd__(self, other):
      return Cone(self.radius + other.radius, self.height+other.height)
   """
   Function Name:
      __str__()

   Description:
      class function to return the string for the object instance.
   
   Parameters:
      None.

   Returns:
      Returns a string containing the radius and height of the Cone's
      instance for which it exists up to two decimal digits.
   """
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
   """
   Function Name:
      __init__()

   Description:
      Constructor for Sphere class inheriting Circle class
      takeing radius of the Sphere for the arguments.
   
   Parameters:
      radius - radius of the Sphere
   
   Returns:
      None
   """
   def __init__(self, radius=0):
      self.radius = radius
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the surface area of
      the Sphere whose radius exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of surface area of the Sphere calculated using the formula
      𝐴 = 4𝐴0 where 𝐴0 is the area of the sphere where the cross-section is the
      largest. 
   """
   def area(self):
      return 4*Circle.area(self)
   """
   Function Name:
      volume()
   
   Description:
      class function to calculate and return the volume of
      the Sphere whose radius exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of volume of the Sphere calculated using the formula
      𝑉 = (4/3)r𝐴0 where 𝐴0 is the area of the sphere where the cross-section is the
      largest. 
   """
   def volume(self):
      return (4/3) * Circle.area(self) * self.radius
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class sphere with the
      radius of current instance and the 
      argument added together.
   
   Parameters:
      other - instance of the class sphere to be added
      together.

   Returns:
      Returns an instance of the class sphere with dimensions
      of both the intstance itself and the argument supplied
      added together.
   """
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
   """
   Function Name:
      __init__()

   Description:
      Constructor for Cube class inheriting equTriangle class
      takeing length of side of the Tetrahedron for the arguments.
   
   Parameters:
      length - length of the side of the Tetrahedron.

   Returns:
      None
   """
   def __init__(self, a=0):
      equTriangle.__init__(self, a)
   """
   Function Name:
      area()

   Description:
      class function to calculate and return the surface area of
      the Tetrahedron whose length of the side exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of area of the Tetrahedron calculated using the formula
      𝐴= 4𝐴0  where 𝐴0 is the area of one of the faces of the Tetrahedron.
   """
   def area(self):
      return 4*equTriangle.area(self)
   """
   Function Name:
      volume()
   
   Description:
      class function to calculate and return the volume of
      the Tetrahedron whose length of side exists in the given instance
   
   Parameters:
      None.

   Returns:
      Returns the value of volume of the Tetrahedron calculated using the formula
      𝑉 = (1/3)h𝐴0, where 𝐴0 is the area of one of the faces of the tetrahedron.
   """
   def volume(self):
      return (1/3) * equTriangle.area(self) * ((2/3)**0.5)*self.a
   """
   Function Name:
      __iadd__()

   Description:
      Overloaded function for standard operator  "+="
      whose result is the instance of class Cube with the
      length of side of Tetrahedron of current instance and the 
      argument added together.
   
   Parameters:
      other - instance of the class Tetrahedron to be added
      together.

   Returns:
      Returns an instance of the class Tetrahedron with the length
      of side of both the intstance itself and the argument
      supplied added together.
   """
   def __iadd__(self, other):
      return Tetrahedron(self.a + other.a)
