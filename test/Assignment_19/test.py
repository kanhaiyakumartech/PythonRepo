import unittest
from src.Assignment_19.util import time_delta


class TestCustomTimeDelta(unittest.TestCase):

    def test_cus_time_delta(self):
        # Test case with two time strings
        t1 = 'Sun 10 Nov 2019 05:30:00 +0000'
        t2 = 'Sun 10 Nov 2019 08:45:00 +0000'

        result = time_delta(t1, t2)
        self.assertEqual(result, '11700')  # Assuming you want to test against a specific value


if __name__ == '__main__':
    unittest.main()
