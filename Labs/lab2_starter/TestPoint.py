import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase): 
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(3,4)
        self.p4 = Point(-3, -4)
        self.p5 = Point(0,0)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""  
        self.assertEqual(self.p1.x, 3)      
        self.assertEqual(self.p1.y, 4)

    def test_eq(self):
        """tests that different points are the same or different"""
        self.assertEqual(self.p1, self.p3)
        self.assertNotEqual(self.p1, self.p2)

    def test_equidistant(self):
        """Tests if points are the same distance"""
        
        self.assertEqual(self.p1.equidistant(self.p4), True)
        self.assertNotEqual(self.p1.equidistant(self.p2), True)

    def test_within(self):
        """Tests if the distances are within the range of a certain distancex"""
        self.assertEqual(Point(3,4).within(1, Point(3.5, 4)), True)

        self.assertNotEqual(self.p2.within((61 ** 1/2),Point(0,0)), True)
    


unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects