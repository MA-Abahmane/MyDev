#!/usr/bin/python3
"""
Class Point
"""

import math


class Point():
    """ Class Point """

    def __str__(self):
        """ Self Print """
        return f'Point: ({self.x}, {self.y})'

    def __init__(self, x=0, y=0):
        """ Constructor """
        self.x = x
        self.y = y

    def display(self):
        """ Display the points coordinates """
        print(f'Point({self.x}, {self.y})')

    def displace(self, dx, dy):
        """ Displace the point """
        self.x += dx
        self.y += dy

    def distance_calc(self, point):
        """ Return the distance between two points """
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
    
    def __add__(self, point):
        """ Add up 2 points and return the result as a new Point """
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)
    
    def __mul__(self, point):
        """ Multiply 2 points and return the product as a new Point """
        x = self.x * point.x
        y = self.y * point.y
        return Point(x, y)


if __name__ == '__main__':
    """ Import control """
    P1 = Point(10, 10)
    P1.display()

    P1.displace(7, 7)
    P1.display()

    P2 = Point(10, 10)
    print(P1.distance_calc(P2))

    print('___-_______-____-____-')


"""
Class Point 3D
"""


class Point3D(Point):
    """ Class Point3D """

    def __init__(self, x, y, z):
        """ Constructor """
        super().__init__(x, y)
        self.z = z

    def display(self):
        """ Displace the point """
        print(f'Point[x:{self.x} y:{self.y} z:{self.z}]')

    def distance_calc(self, point):
        """ Return the distance between two points """

        if isinstance(point, Point):
            return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        elif isinstance(point, Point3D):
            return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)
        else:
            raise ValueError('Invalid Point Object')


if __name__ == '__main__':
    """ Import control """
    P3 = Point3D(1, 1, 1)
    P3.display()

    P3.displace(2, 2)
    P3.display()

    P4 = Point3D(7, 7, 7)
    print(P1.distance_calc(P4))

    print(P1 + P2)
