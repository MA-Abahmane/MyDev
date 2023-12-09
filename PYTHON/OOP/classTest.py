#!/usr/bin/python3

import unittest
from Point import Point, Point3D
from Rectangle import Rectangle

class classTests(unittest.TestCase):

    def setUp(self):
        """ Create instances before each test """
        self.P1 = Point(1, 2)
        self.P2 = Point3D(3, 4, 5)
        self.R1 = Rectangle(self.P1, 10, 20)

    def test_creation(self):
        """ Test class instance creation """
        self.assertTrue(isinstance(self.P1, Point))
        self.assertTrue(isinstance(self.P2, Point3D))
        self.assertTrue(isinstance(self.R1, Rectangle))

    def test_Documentation(self):
        """ Documentation Display """
        self.assertEqual(type(self.P1.__doc__), str)
        self.assertEqual(type(self.P2.displace.__doc__), str)
        self.assertEqual(type(self.R1.__init__.__doc__), str)

    def test_ObjDictionary(self):
        """ Object Dictionary representation """
        self.assertNotEqual(self.P2.__dict__, {})
        self.assertNotEqual(self.R1.__dict__, {})

    def test_staticmethod(self):
        """ Call Static method """
        self.assertEqual(Rectangle.HowToSurface(), self.R1.HowToSurface())

    def test_operations(self):
        """ Object Operations """
        P3 = self.P1 + self.P2
        self.assertEqual(P3.x, (self.P1.x + self.P2.x))
        self.assertEqual(P3.y, (self.P1.y + self.P2.y))

        Px = self.P1 * self.P2
        self.assertEqual(Px.x, (self.P1.x * self.P2.x))
        self.assertEqual(Px.y, (self.P1.y * self.P2.y))

        R2 = Rectangle(self.P1, 10, 40)
        R3 = Rectangle(self.P2, 20, 40)
        self.assertTrue(self.R1 == R2)
        self.assertFalse(R2 == R3)


if __name__ == '__main__':
    unittest.main()
