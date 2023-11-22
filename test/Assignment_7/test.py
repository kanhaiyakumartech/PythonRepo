import unittest
from src.Assignment_7.util import format_numbers

class TestFormatNumbers(unittest.TestCase):
    def test_format_numbers(self):
        self.assertEqual(format_numbers(5), [('1', ' 1', ' 1', ' 1'),
                                              ('2', ' 2', ' 2', '10'),
                                              ('3', ' 3', ' 3', '11'),
                                              ('4', ' 4', ' 4', '100'),
                                              ('5', ' 5', ' 5', '101')])

if __name__ == '__main__':
    unittest.main()
