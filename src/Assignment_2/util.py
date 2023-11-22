def sum_of_marks(d, student_name):
    for name, scores in d.items():
        if student_name == name:
            percentage = sum(scores) / len(scores)
            print("The average percentage for {} is: {:.2f}%".format(name, percentage))
            return percentage

    print("Student with name {} not found.".format(student_name))
    return None
