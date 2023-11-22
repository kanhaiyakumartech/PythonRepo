import unittest
from src.Assignment_4.util import My_mutate_string
class TestMutateString(unittest.TestCase):
    def test_mutate_string(self):
        self.assertEqual(My_mutate_string("hello", 1, "a"), "hallo")
        self.assertEqual(My_mutate_string("world", 3, "d"), "wordd")

if __name__ == '__main__':
    unittest.main()
