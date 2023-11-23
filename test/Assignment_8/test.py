# unittest.py

import unittest
from src.Assignment_8.util import calculate_average_marks

class TestCalculateAverageMarks(unittest.TestCase):
    def test_calculate_average_marks(self):
        # Assuming a test case where there are 3 students with marks 90, 85, and 95
        nbr_students = 3
        student_data = "NAME AGE MARKS"
        input_data = "John 20 90\nAlice 22 85\nBob 21 95\n"

        with unittest.mock.patch('builtins.input', side_effect=input_data.split()):
            result = calculate_average_marks(nbr_students, student_data.split())

        self.assertEqual(result, 90.0)

if __name__ == '__main__':
    unittest.main()
