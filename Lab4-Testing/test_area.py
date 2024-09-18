# a way to run the unit test using terminal command
# python -m unittest test_area.py
# dot means pass & F means fail on the first line of the result

from unittest import TestCase
import area

class TestShapeAreas(TestCase):     # make sure to pass TestCase here

    def test_triangle_area(self):   # each test should start with "test"
        # A triangle with height 4 and base 6 should have area 10
        self.assertEqual(10, area.triangle_area(4, 5))

    def test_triangle_area_floating_point(self):
        # for floating-point number, use "AlmostEqual" instead of "Equal" to compare the values
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))


    # make sure to test edge cases! (empty string, empty list, 0 ...)

    # tests for negative integers
    # assuming this program should raise a ValueError if either or both height and base are negative
    # we need to use context manager to test something raises an error

    def test_triangle_area_negative_integer(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-10, 5)

        with self.assertRaises(ValueError):
            area.triangle_area(7, -3)

        with self.assertRaises(ValueError):
            area.triangle_area(-4, -6)

    # test for 0 value
    # assuming 0 is a valid value in this program, it should return 0 area if either or both height and base are 0

    def test_triangle_area_zero(self):
        self.assertEqual(0, area.triangle_area(0, 5))
        self.assertEqual(0, area.triangle_area(7, 0))
        self.assertEqual(0, area.triangle_area(0, 0))

