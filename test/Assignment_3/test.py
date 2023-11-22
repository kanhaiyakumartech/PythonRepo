# unittest.py
import unittest
from src.Assignment_3.util import second_largest_element

class TestSecondLargestElement(unittest.TestCase):

    def test_second_largest_element(self):
        self.assertEqual(second_largest_element([3, 1, 4, 4, 2, 6]), 4)



if __name__ == '__main__':
    unittest.main()
