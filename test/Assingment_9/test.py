# unittest.py

import unittest
from src.Assingment_9.util import find_max_of_min_values

class TestFindMaxOfMinValues(unittest.TestCase):
    def test_find_max_of_min_values(self):
        # Test case with a 2x3 matrix
        matrix = [['1', '2', '3'], ['4', '5', '6']]

        result = find_max_of_min_values(matrix)

        # Expected result for the given test case
        expected_result = 4

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
