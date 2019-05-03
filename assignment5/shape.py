#!/usr/bin/env python3

"""
This is an abstract super class for geometic shapes. The methods of
this class need to be defined in the sub classes; otherwise, an error
will be raised to alert the user.
"""
class Shape:
    def delegate(self):
        self.area()
        self.perimeter()
        self.volume()
    def area(self):
        raise NotImplementedError('area must be defined!')
    def perimeter(self):
        raise NotImplementedError('perimeter must be defined!')
    def volume(self):
        raise NotImplementedError('volume must be defined!')
