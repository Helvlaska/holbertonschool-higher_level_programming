#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 1, 0]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 10, 2]), 10)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_all_negative(self):
        self.assertEqual(max_integer([-3, -1, -7]), -1)

    def test_mixed_with_zero(self):
        self.assertEqual(max_integer([-1, 0, 3]), 3)

    def test_identical_elements(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.5, 3.3]), 3.3)

    def test_mix_int_float(self):
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_string_input(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")


if __name__ == '__main__':
    unittest.main()
