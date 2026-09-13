import unittest

from src.math_utils import clamp


class TestClamp(unittest.TestCase):
    def test_value_below_minimum(self):
        self.assertEqual(clamp(-1, 0, 10), 0)

    def test_value_above_maximum(self):
        self.assertEqual(clamp(11, 0, 10), 10)

    def test_value_within_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_value_equal_to_minimum(self):
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_value_equal_to_maximum(self):
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_minimum_equal_to_maximum(self):
        self.assertEqual(clamp(5, 5, 5), 5)

    def test_minimum_greater_than_maximum(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
