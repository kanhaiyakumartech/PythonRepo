# util.py

from collections import namedtuple

def calculate_average_marks(nbr_students, student_data):
    sheet = namedtuple("sheet", student_data)
    marks = 0

    for _ in range(nbr_students):
        marks += int(sheet._make(input().split()).MARKS)

    return round(marks / nbr_students, 2)
