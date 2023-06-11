from Rectangle import Rectangle 
import unittest

class TestRectangleCase(unittest.TestCase):

    def setUp(self):
        self.rectangle1 = Rectangle(1, 2)
        self.rectangle2 = Rectangle(3)

    def test_string_view(self):
        self.assertEqual(str(self.rectangle1),'Rectangle(1, 2)')
        self.assertEqual(str(self.rectangle2),'Rectangle(3, 3)')

    def test_comparing(self):
        self.assertTrue(self.rectangle2 > self.rectangle1)

    def test_diff(self):
        self.assertEqual(self.rectangle2 - self.rectangle1,Rectangle(1.5, 1.5))

    def test_sum(self):
        self.assertEqual(self.rectangle2 + self.rectangle1,Rectangle(4.5, 4.5))
        self.assertEqual(self.rectangle1 + self.rectangle2,Rectangle(3.0, 6.0))

    def test_negative_length_error(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

    # >>> print(rectangle1) 
    # Rectangle(1, 2)
    # >>> print(rectangle2)
    # Rectangle(3, 3)
    # >>> print(rectangle2 > rectangle1)
    # True
    # >>> print(rectangle2 - rectangle1)
    # Rectangle(1.5, 1.5)
    # >>> print(rectangle1 + rectangle2)
    # Rectangle(3.0, 6.0)
    # >>> rectangle3 = Rectangle(-1, 2)
    # Traceback (most recent call last):
    # ...
    # ValueError: -1 меньше 0
    # """