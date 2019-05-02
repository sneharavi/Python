#!/usr/bin/python3

from shape3 import *

N = 50
LINE = '=' * N  # It's used in drawing a line between
                # individual segments.

"""
This external routine is to print out certain parameters of
some of the two- or three-dimensional geometric shapes.
"""

def Print ( name, shape, flag = True ):
    print ( name, end = ': ' ); print ( shape )
    print ( 'area = %.2f' % shape.area ( ) ) 
    if flag: print ( 'perimeter = %.2f' % shape.perimeter ( ) ) 
    else: print ( 'volume = %.2f' % shape.volume ( ) ) 
    print ( )

"""Test rectangle objects"""
print ( '\nRectangle:' )
r1 = Rectangle ( 7.5, 2.5 ); r2 = Rectangle ( )
Print ( 'r1', r1 ); Print ( 'r2', r2 )
r2 += r1; Print ( 'r2', r2 )
print ( LINE, '\n' )

"""Test circle objects"""
print ( 'Circle:' )
c1 = Circle ( 2.5 ); c2 = Circle ( 5 )
Print ( 'c1', c1 ); Print ( 'c2', c2 )
c1 += c2; Print ( 'c1', c1 )
print ( LINE, '\n' )

"""Test triangle objects"""
print ( 'Triangle:' )
t1 = Triangle ( 5.1, 12.2, 13.3 ); Print ( 't1', t1 )
t1 += t1; Print ( 't1', t1 )
print ( LINE, '\n' )

"""Test square objects - inherited from rectangular objects"""
print ( 'Square:' )
s1 = Square ( 2.5 ); Print ( 's1', s1 )
s1 += s1; Print ( 's1', s1 )
print ( LINE, '\n' )

"""Test right-triangle objects - inherited from  triangular objects"""
print ( 'Right Triangle:' )
rt1 = rightTriangle( 5, 12 ); Print ( 'rt1', rt1 )
rt1 += rt1; Print ( 'rt1', rt1 )
print ( LINE, '\n' )

"""Test equilateral-triangle objects - inherited from triangular objects"""
print ( 'Equilateral Triangle:' )
et1 = equTriangle ( 5 ); Print ( 'et1', et1 )
et1 += et1; Print ( 'et1', et1 )
print ( LINE, '\n' )

"""Test box objects - inherited from rectangle objects"""
print ( 'Box:' )
b1 = Box ( 3, 4, 5 ); Print ( 'b1', b1, False )
b1 += b1; Print ( 'b1', b1, False )
print ( LINE, '\n' )

"""Test cube objects - inherited from square objects"""
print ( 'Cube:' )
cu1 = Cube ( 2.5 ); Print ( 'cu1', cu1, False )
cu1 += cu1; Print ( 'cu1', cu1, False )
print ( LINE, '\n' )

"""Test cylinder objects - inherited from circle objects"""
print ( 'Cylinder:' )
cy1 = Cylinder ( 2.5, 5 ); Print ( 'cy1', cy1, False )
cy1 += cy1; Print ( 'cy1', cy1, False )
print ( LINE, '\n' )

"""Test cone objects - inherited from circle objects"""
print ( 'Cone:' )
co1 = Cone ( 2.5, 5 ); co2 = Cone ( 3.75, 4.25 )
Print ( 'co1', co1, False ); Print ( 'co2', co2, False )
co2 += co1; Print ( 'co2', co2, False )
print ( LINE, '\n' )

"""Test sphere objects - inherited from circle objects"""
print ( 'Sphere:' )
sp1 = Sphere ( 2.5 ); Print ( 'sp1', sp1, False )
sp1 += sp1; Print ( 'cp1', sp1, False )
print ( LINE, '\n' )

"""Test tetrahedron objects - inherited from equilateral-triangle objects"""
print ( 'Tetrahedron:' )
te1 = Tetrahedron ( 5 ); Print ( 'te1', te1, False )
te2 = Tetrahedron ( ); Print ( 'te2', te2, False )
te2 += te1; Print ( 'te2', te2, False )
