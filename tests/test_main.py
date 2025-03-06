import unittest
from main import Circle, Rectangle, Triangle, Color

class TestFigures(unittest.TestCase):
    pass

def test_circle(self):
    circle = Circle(0, 0, 5, Color.RED, "2023-01-01")
    self.assertEqual(circle.centerX, 0)
    self.assertEqual(circle.centerY, 0)
    self.assertEqual(circle.radius, 5)

def test_rectangle(self):
    rectangle = Rectangle(0, 0, 10, 10, Color.BLUE, "2023-01-01")
    self.assertEqual(rectangle.x1, 0)
    self.assertEqual(rectangle.y1, 0)
    self.assertEqual(rectangle.x2, 10)
    self.assertEqual(rectangle.y2, 10)

def test_triangle(self):
    triangle = Triangle(0, 0, 10, 0, 5, 10, Color.GREEN, "2023-01-01")
    self.assertEqual(triangle.x1, 0)
    self.assertEqual(triangle.y1, 0)
    self.assertEqual(triangle.x2, 10)
    self.assertEqual(triangle.y2, 0)


def test_invalid_color(self):
    with self.assertRaises(KeyError):
        Circle(0, 0, 5, "InvalidColor", "2023-01-01")


def test_invalid_radius(self):
    with self.assertRaises(ValueError):
        Circle(0, 0, -5, Color.RED, "2023-01-01")

def test_invalid_coordinates(self):
    with self.assertRaises(ValueError):
        Rectangle(-10, 0, 10, 10, Color.BLUE, "2023-01-01")


