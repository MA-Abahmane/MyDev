#!/usr/bin/python3
"""
Class Rectangle
"""

from Point import Point


class Rectangle:
    """ Class Rectangle """

    def __str__(self):
        """ Self Print """
        return f'The rectangle whose corner is ({self.topLeft.x}, {self.topLeft.y}), height {self.height} and width {self.width}'

    def __init__(self, point, width, height):
        """ Constructor """
        self.topLeft = point
        self.width, self.height = width, height

    def display(self):
        """ Display Top|left Rectangle corner Points coordinates, Width and Height """
        print(f'TopLeft: ({self.topLeft.x}, {self.topLeft.y})')
        print(f'Width  : {self.width}')
        print(f'Height : {self.height}')

    def surface(self):
        """ Return the rectangles surface """
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter perimeter """
        return (self.width + self.height) * 2

    @staticmethod
    def HowToSurface():
        """ Display text """
        print('The formula for calculating the surface area of a rectangle is: area = height * width')

    def __eq__(self, rect):
        """ Check if two Rectangles are Equal; return Bool """
        return (self.height and self.width and self.topLeft.x and self.topLeft.y) == (rect.height and rect.width and rect.topLeft.x and rect.topLeft.y)



if __name__ == '__main__':
    P1 = Point(20, 20)
    R1 = Rectangle(P1, 11, 22)

    R1.display()
    R1.topLeft.displace(10, 10)
    print()

    R1.display()
    print()

    print(f"""Rectangle
    Surface  : {R1.surface()}
    Perimeter: {R1.perimeter()}
    """)


