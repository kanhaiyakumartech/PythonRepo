import unittest
from src.Assignment_10.util import average_marks


class TestCalculateAverageMarks(unittest.TestCase):

    def test_average_marks(self):
        # Test case with three students
        num_students = 3
        fields = ['MARKS', 'CLASS', 'NAME', 'ID']
        student_data = lambda: ['92', '1', 'John', '1']

        result = average_marks(num_students, fields, student_data)
        self.assertAlmostEqual(result, 92.0, places=2)  # Assuming you want to test against a specific value


if __name__ == '__main__':
    unittest.main()

