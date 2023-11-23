# Test Code For Calendra program
import unittest
from src.Assignment_5.util import Check_Day_Name

class TestGetDayName(unittest.TestCase):

    def test_Now_Testing_is_done(self):
        self.assertEqual(Check_Day_Name(11, 23, 2023), "THURSDAY")


if __name__ == '__main__':
    unittest.main()
