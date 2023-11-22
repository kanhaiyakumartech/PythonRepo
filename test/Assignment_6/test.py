import unittest
from src.Assignment_6.util import merge_the_tools

class Test_and_Merge_The_Tools(unittest.TestCase):
    def test_and_merge_the_tools(self):
        self.assertEqual(list(merge_the_tools("AABCAAADA", 3)), ['AB', 'CA', 'AD'])

if __name__ == '__main__':
    unittest.main()
