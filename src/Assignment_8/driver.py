# driver.py

from util import calculate_average_marks

if __name__ == "__main__":
    nbr_students = int(input("Enter the number of students: "))
    student_data = input("Enter space-separated student field names: ").split()

    average_marks = calculate_average_marks(nbr_students, student_data)

    print(f"The average marks of {nbr_students} students is: {average_marks}")
