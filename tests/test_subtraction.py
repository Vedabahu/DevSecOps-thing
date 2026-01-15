import unittest
from cal import sub

class TestSubtraction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sub(10, 4), 6)

    def test_negative_numbers(self):
        self.assertEqual(sub(-2, -5), 3)

    def test_mixed_sign_numbers(self):
        self.assertEqual(sub(-3, 5), -8)

    def test_zero(self):
        self.assertEqual(sub(0, 10), -10)
        self.assertEqual(sub(0, 0), 0)

if __name__ == "__main__":
    unittest.main()