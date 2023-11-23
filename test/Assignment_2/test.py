# unittest.py
import unittest
from src.Assignment_2.util import calculate_percentage

class TestCalculatePercentage(unittest.TestCase):
    def test_percentage_calculation(self):
        self.assertEqual(calculate_percentage([90, 85, 78]), 84.33)
        self.assertEqual(calculate_percentage([75, 88, 92]), 85.00)

if __name__ == '__main__':
    unittest.main()
