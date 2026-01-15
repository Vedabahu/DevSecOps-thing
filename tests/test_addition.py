import unittest
from cal import add


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(3, 4), 7)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -5), -7)

    def test_mixed_sign_numbers(self):
        self.assertEqual(add(-3, 5), 2)

    def test_zero(self):
        self.assertEqual(add(0, 10), 10)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
