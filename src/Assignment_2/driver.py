# This code for find the percentage taking a variables from user
from util import calculate_percentage

if __name__ == '__main__':
    # Enter the number of students
    n = int(input())

    # Here we store all the marks
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # Now we enter the name of the student for whom we want the percentage
    query_name = input()

    # Calculate and print the percentage
    output = list(student_marks[query_name])
    percentage = calculate_percentage(output)
    print("%.2f" % percentage)
